from sqlalchemy.orm import Session
from app.payments.model import Payment
from app.payments.schema import PaymentCreate
from app.merchants.model import Merchant
from app.models.user import User
from app.mpesa.service import stk_push
def create_payment(
        db: Session,
        payment: PaymentCreate,
        current_user: User,
):
    
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None
    
    mpesa_response = stk_push(
        phone_number=payment.phone_number,
        amount=int(payment.amount),
        account_reference=payment.reference,
        transaction_desc=payment.description or "Payment",
        
    )
    print("M-Pesa Response:" , mpesa_response)
    
    new_payment = Payment(
        merchant_id = merchant.id,
        amount=payment.amount,
        phone_number=payment.phone_number,
        reference=payment.reference,
        description=payment.description,
        status="PENDING",
        checkout_request_id=mpesa_response.get("CheckoutRequestID"),
        merchant_request_id=mpesa_response.get("MerchantRequestID"),
)
    
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment