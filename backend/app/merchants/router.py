from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User

from app.merchants.service import (
    create_merchant,
    get_merchant_profile,
    update_merchant_profile,
)

from app.merchants.schema import (
    MerchantCreate,
    MerchantResponse,
    MerchantProfileUpdate,
)

router = APIRouter(
    prefix="/merchant",
    tags=["Merchant"],
)


@router.post(
    "",
    response_model=MerchantResponse,
)
def create_business(
    merchant: MerchantCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = create_merchant(
        db,
        merchant,
        current_user,
    )

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Merchant profile already exists",
        )

    return result


@router.get(
    "/profile",
    response_model=MerchantResponse,
)
def profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    merchant = get_merchant_profile(
        db,
        current_user,
    )
    

    if merchant is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant not found",
        )
    

    print("Merchant:", merchant)
    print("Verified:", merchant.is_verified)
    print("Type:", type(merchant.is_verified))
    

    return merchant


@router.put(
    "/profile",
    response_model=MerchantResponse,
)
def update_profile(
    merchant_data: MerchantProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    merchant = update_merchant_profile(
        db,
        current_user,
        merchant_data,
    )

    if merchant is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant not found",
        )

    return merchant