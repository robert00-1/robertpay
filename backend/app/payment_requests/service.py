from sqlalchemy.orm import Session
from datetime import datetime

from app.payment_requests.model import PaymentRequest
from app.payment_requests.schema import PaymentRequestCreate
from app.models.user import User
from app.merchants.model import Merchant
from app.mpesa.service import stk_push
from app.payments.model import Payment
from app.merchant_settings.model import MerchantSettings

def create_payment_request(
    db: Session,
    request: PaymentRequestCreate,
    current_user: User,
):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None

    payment_request = PaymentRequest(
        merchant_id=merchant.id,
        customer_name=request.customer_name,
        customer_phone=request.customer_phone,
        customer_email=request.customer_email,
        amount=request.amount,
        reference=request.reference,
        description=request.description,
        status="PENDING",
        created_at=datetime.utcnow(),
    )

    db.add(payment_request)
    db.commit()
    db.refresh(payment_request)

    return payment_request


def get_payment_requests(
    db: Session,
    current_user: User,
):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return []

    return (
        db.query(PaymentRequest)
        .filter(PaymentRequest.merchant_id == merchant.id)
        .order_by(PaymentRequest.created_at.desc())
        .all()
    )


def get_payment_request(
    db: Session,
    payment_request_id: int,
    current_user: User,
):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None

    return (
        db.query(PaymentRequest)
        .filter(
            PaymentRequest.id == payment_request_id,
            PaymentRequest.merchant_id == merchant.id,
        )
        .first()
    )


def send_payment_request(
    db: Session,
    payment_request_id: int,
    current_user: User,
):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None

    payment_request = (
        db.query(PaymentRequest)
        .filter(
            PaymentRequest.id == payment_request_id,
            PaymentRequest.merchant_id == merchant.id,
        )
        .first()
    )

    if payment_request is None:
        return None

    if payment_request.status != "PENDING":
        return "ALREADY_PROCESSED"
    merchant_settings = (
        db.query(MerchantSettings)
        .filter(
            MerchantSettings.merchant_id == merchant.id,
        )
        .first()
    )
    if merchant_settings is None:
        return {
            "error": "Merchant payment settings not configured."
        }
    print("\n========== USING MERCHANT SETTINGS ==========")
    print("Merchant ID:", merchant.id)
    print("Business Name:", merchant_settings.business_name)
    print("PayBill:", merchant_settings.paybill_number)
    print("Environment:", merchant_settings.environment)
    print("Callback URL:", merchant_settings.callback_url)
    print("=============================================\n")


    response = stk_push(
    merchant_settings=merchant_settings,
    phone_number=payment_request.customer_phone,
    amount=payment_request.amount,
    account_reference=payment_request.reference,
    transaction_desc=payment_request.description or "RobertPay Payment",
)
   
    if response.get("ResponseCode") == "0":
        payment = Payment(
            merchant_id=merchant.id,
            payment_request_id=payment_request.id,
            amount=payment_request.amount,
            phone_number=payment_request.customer_phone,
            reference=payment_request.reference,
            description=payment_request.description,
            status="PENDING",
            checkout_request_id=response.get("CheckoutRequestID"),
            merchant_request_id=response.get("MerchantRequestID"),
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

    return response