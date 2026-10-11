
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
    try:
        # Find an existing merchant for this user.
        existing = (
            db.query(Merchant)
            .filter(Merchant.user_id == current_user.id)
            .first()
        )

        if existing:
            new_merchant = existing
        else:
            new_merchant = Merchant(
                business_name=merchant.business_name,
                business_email=merchant.business_email,
                business_phone=merchant.business_phone,
                business_address=merchant.business_address,
                kra_pin=merchant.kra_pin,
                user_id=current_user.id,
            )
            db.add(new_merchant)
            db.flush()

        # Create a wallet only if one does not already exist.
        wallet = (
            db.query(Wallet)
            .filter(Wallet.merchant_id == new_merchant.id)
            .first()
        )

        if wallet is None:
            wallet = Wallet(
                merchant_id=new_merchant.id,
                balance=0,
                currency="KES",
                status="ACTIVE",
            )
            db.add(wallet)

        # Create API keys only if they do not already exist.
        api_key = (
            db.query(ApiKey)
            .filter(ApiKey.merchant_id == new_merchant.id)
            .first()
        )

        if api_key is None:
            api_key = ApiKey(
                merchant_id=new_merchant.id,
                publishable_key="pk_" + secrets.token_hex(16),
                secret_key="sk_" + secrets.token_hex(32),
                environment="SANDBOX",
                status="ACTIVE",
            )
            db.add(api_key)

        # Save all missing records together.
        db.commit()
        db.refresh(new_merchant)

        return new_merchant

    except Exception:
        db.rollback()
        raise


def get_merchant_profile(
    db: Session,
    current_user: User,
):
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
