from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.payments.model import Payment
from app.wallets.model import Wallet
from app.payment_requests.model import PaymentRequest

router = APIRouter(
    prefix="/mpesa",
    tags=["M-Pesa"],
)


@router.post("/callback")
async def mpesa_callback(
    payload: dict,
    db: Session = Depends(get_db),
):
    print("\n========== CALLBACK ==========")
    print(payload)
    print("==============================\n")

    callback = payload["Body"]["stkCallback"]

    checkout_request_id = callback["CheckoutRequestID"]
    result_code = callback["ResultCode"]
    result_desc = callback["ResultDesc"]

    payment = (
        db.query(Payment)
        .filter(
            Payment.checkout_request_id == checkout_request_id
        )
        .first()
    )

    if payment is None:
        return {
            "ResultCode": 0,
            "ResultDesc": "Payment not found",
        }
    if payment.status == "SUCCESS":
        return {
            "ResultCode": 0,
            "ResultDesc": "Already processed",
        }

    payment.result_code = result_code
    payment.result_desc = result_desc

    if result_code == 0:
        metadata = callback["CallbackMetadata"]["Item"]

        values = {}

        for item in metadata:
            values[item["Name"]] = item.get("Value")

        payment.status = "SUCCESS"
        payment.mpesa_receipt_number = values.get("MpesaReceiptNumber")

        transaction_date = str(values["TransactionDate"])

        payment.paid_at = datetime.strptime(
            transaction_date,
            "%Y%m%d%H%M%S",
        )
        payment_request = (
            db.query(PaymentRequest)
            .filter(
                PaymentRequest.id == payment.payment_request_id
            )
            .first()
        )
        if payment_request:
            payment_request.status = "PAID"
            payment_request.paid_at = payment.paid_at

        print("Payment merchant_id:", payment.merchant_id)

        wallet = (
            db.query(Wallet)
            .filter(
                Wallet.merchant_id == payment.merchant_id
            )
            .first()
        )
        print("Wallet:", wallet)

        if wallet is None:
            return {
                "ResultCode": 0,
                "ResultDesc": "Wallet not found",
            }
        
        print("Balance before:", wallet.balance)
        print("Payment amount:", payment.amount)

        wallet.balance = (wallet.balance or 0) + payment.amount

        print("Balance after:", wallet.balance)

        from app.transactions.model import Transaction

        transaction = Transaction(
            wallet_id=wallet.id,
            payment_id=payment.id,
            type="CREDIT",
            amount=payment.amount,
            balance_after=wallet.balance,
            reference=payment.reference,
            description=payment.description,
            status="SUCCESS",
        )
        db.add(transaction)

    else:
        payment.status = "FAILED"

    db.commit()

    print("Wallet committed")

    return {
        "ResultCode": 0,
        "ResultDesc": "Accepted",
    }
