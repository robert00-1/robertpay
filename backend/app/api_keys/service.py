import secrets

from sqlalchemy.orm import Session

from app.api_keys.model import ApiKey
from app.merchants.model import Merchant
from app.models.user import User


def get_api_keys(
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

    api_key = (
        db.query(ApiKey)
        .filter(ApiKey.merchant_id == merchant.id)
        .first()
    )

    if api_key:
        return api_key

    api_key = ApiKey(
        merchant_id=merchant.id,
        publishable_key=f"pk_test_{secrets.token_hex(16)}",
        secret_key=f"sk_test_{secrets.token_hex(32)}",
        environment="SANDBOX",
        status="ACTIVE",
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return api_key


def regenerate_api_keys(
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

    api_key = (
        db.query(ApiKey)
        .filter(ApiKey.merchant_id == merchant.id)
        .first()
    )

    if api_key is None:
        api_key = ApiKey(
            merchant_id=merchant.id,
            publishable_key=f"pk_test_{secrets.token_hex(16)}",
            secret_key=f"sk_test_{secrets.token_hex(32)}",
            environment="SANDBOX",
            status="ACTIVE",
        )
        db.add(api_key)
    else:
        api_key.publishable_key = f"pk_test_{secrets.token_hex(16)}"
        api_key.secret_key = f"sk_test_{secrets.token_hex(32)}"
        api_key.environment = "SANDBOX"
        api_key.status = "ACTIVE"

    db.commit()
    db.refresh(api_key)

    return api_key