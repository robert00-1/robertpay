from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.merchant_settings.schema import (
    MerchantSettingsCreate,
    MerchantSettingsUpdate,
    MerchantSettingsResponse,
)

from app.merchant_settings.service import (
    create_settings,
    get_settings,
    update_settings,
)

router = APIRouter(
    prefix="/merchant-settings",
    tags=["Merchant Settings"],
)

@router.post(
    "",
    response_model=MerchantSettingsResponse,
)
def create_merchant_settings(
    request: MerchantSettingsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = create_settings(
        db,
        request,
        current_user
    )
    if settings is None:
        raise HTTPException(
            status_code=404,
            detail="Merchant profile not found",
        )
    return settings
@router.get(
    "",
    response_model=MerchantSettingsResponse,
)
def get_merchant_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = get_settings(
        db,
        current_user,
    )
    if settings is None:
        raise HTTPException(
            status_code=404,
            detail="Settings not found"
        )
    return settings

@router.put(
    "",
    response_model=MerchantSettingsResponse,
)
def update_merchant_settings(
    request: MerchantSettingsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    settings = update_settings(
        db,
        request,
        current_user,
    )
    if settings is None:
        raise HTTPException(
            status_code=404,
            detail="Settings not found",
        )
    return settings