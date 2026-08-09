from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.payment_requests.schema import (
    PaymentRequestCreate,
    PaymentRequestResponse,
)

from app.payment_requests.service import (
    create_payment_request,
    get_payment_requests,
    get_payment_request,
    send_payment_request,
)

router = APIRouter(
    prefix="/payment-requests",
    tags=["Payment Requests"],
)


@router.post("")
def create_request(
    request: PaymentRequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    payment_request = create_payment_request(
        db,
        request,
        current_user,
    )

    if payment_request is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found",
        )
    result = send_payment_request(
        db,
        payment_request.id,
        current_user,
    )

    return{
       "payment_request": payment_request,
       "stk_response" : result, 
    }
    


@router.get(
    "",
    response_model=list[PaymentRequestResponse],
)
def list_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_payment_requests(
        db,
        current_user,
    )


@router.get(
    "/{payment_request_id}",
    response_model=PaymentRequestResponse,
)
def get_request(
    payment_request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    payment_request = get_payment_request(
        db,
        payment_request_id,
        current_user,
    )

    if payment_request is None:
        raise HTTPException(
            status_code=404,
            detail="Payment request not found",
        )

    return payment_request


@router.post("/{payment_request_id}/send")
def send_request(
    payment_request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = send_payment_request(
        db,
        payment_request_id,
        current_user,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Payment request not found",
        )

    if result == "ALREADY_PROCESSED":
        raise HTTPException(
            status_code=400,
            detail="Payment request already processed",
        )

    return result