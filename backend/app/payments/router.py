from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.payments.schema import PaymentCreate, PaymentResponse
from app.payments.service import create_payment


router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)

@ router.post("", response_model=PaymentResponse)
def create_new_payment(
    payment: PaymentCreate,
    db:Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_payment = create_payment(
        db,
        payment,
        current_user,
    )

    if new_payment is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant not found",
        )
    
    return new_payment