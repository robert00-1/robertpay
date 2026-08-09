from sqlalchemy.orm import Session
import secrets

from app.merchants.model import Merchant
from app.merchants.schema import (
    MerchantCreate,
    MerchantProfileUpdate,
)
from app.models.user import User
from app.wallets.model import Wallet
from app.api_keys.model import ApiKey


def create_merchant(
    db: Session,
    merchant: MerchantCreate,
    current_user: User,
):
    existing = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if existing:
        return None

    new_merchant = Merchant(
        business_name=merchant.business_name,
        business_email=merchant.business_email,
        business_phone=merchant.business_phone,
        business_address=merchant.business_address,
        kra_pin=merchant.kra_pin,
        user_id=current_user.id,
    )

    db.add(new_merchant)
    db.commit()
    db.refresh(new_merchant)

    # Create wallet
    wallet = Wallet(
        merchant_id=new_merchant.id,
        balance=0,
        currency="KES",
        status="ACTIVE",
    )

    db.add(wallet)
    db.commit()
    db.refresh(wallet)

    # Create API keys
    api_key = ApiKey(
        merchant_id=new_merchant.id,
        public_key="pk_" + secrets.token_hex(16),
        secret_key="sk_" + secrets.token_hex(32),
        status="ACTIVE",
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return new_merchant


def get_merchant_profile(
    db: Session,
    current_user: User,
):
    """
    Return the logged-in user's merchant profile.
    """
    return (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )


def update_merchant_profile(
    db: Session,
    current_user: User,
    merchant_data: MerchantProfileUpdate,
):
    """
    Update the logged-in merchant's profile.
    """
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None

    updates = merchant_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(merchant, key, value)

    db.commit()
    db.refresh(merchant)

    return merchant