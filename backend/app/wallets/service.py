from sqlalchemy.orm import Session
from  decimal import Decimal
from app.wallets.model import Wallet
from app.merchants.model import Merchant
from app.models.user import User
from app.transactions.model import Transaction
import uuid

def get_wallet(db: Session, current_user: User):
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None

    wallet = (
        db.query(Wallet)
        .filter(Wallet.merchant_id == merchant.id)
        .first()
    )

    return wallet


def deposit_money(
        db: Session,
        current_user: User,
        amount: Decimal,
):
    
    merchant = (
        db.query(Merchant)
        .filter(Merchant.user_id == current_user.id)
        .first()
    )

    if merchant is None:
        return None
    
    wallet = (
        db.query(Wallet)
        .filter(Wallet.merchant_id == merchant.id)
        .first()
    )

    if wallet is None:
        return None
    
    wallet.balance += amount

    transaction = Transaction(
        wallet_id=wallet.id,
        amount=amount,
        type="DEPOSIT",
        balance_after=wallet.balance,
        
        reference=str(uuid.uuid4()),
        status="SUCCESS"

    )
    db.add(transaction)

    db.commit()
    db.refresh(wallet)

    return wallet
