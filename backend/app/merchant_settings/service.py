from sqlalchemy.orm import Session

from app.merchant_settings.model import MerchantSettings
from app.merchants.model import Merchant
from app.models.user import User
from app.merchant_settings.schema import (
    MerchantSettingsCreate,
    MerchantSettingsUpdate,
)

def create_settings(
        db: Session,
        request: MerchantSettingsCreate,
        current_user: User,
):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )
    if merchant is None:
        return None
    
    existing = (
        db.query(MerchantSettings)
        .filter(
            MerchantSettings.merchant_id == merchant.id
        )
        .first()
    )

    if existing:
        return existing
    
    settings = MerchantSettings(
        merchant_id=merchant.id,
        business_name=request.business_name,
        payment_type=request.payment_type,
        paybill_number=request.paybill_number,
        account_number=request.account_number,
        consumer_key=request.consumer_key,
        consumer_secret=request.consumer_secret,
        passkey=request.passkey,
        callback_url=request.callback_url,
        environment=request.environment,
        is_active=True,
    )
    db.add(settings)
    db.commit()
    db.refresh(settings)

    return settings

def get_settings(
        db: Session,
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
        db.query(MerchantSettings)
        .filter(
            MerchantSettings.merchant_id == merchant.id
        )
        .first()
    )
def update_settings(
        db: Session,
        request: MerchantSettingsUpdate,
        current_user: User,
):
    
    settings = get_settings(
        db,
        current_user,
    )
    if settings is None:
        return None
    
    data = request.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(settings, key, value)

    db.commit()
    db.refresh(settings)

    return settings    
