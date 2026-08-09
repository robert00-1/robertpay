from sqlalchemy.orm import Session
from sqlalchemy import func

from app.transactions.model import Transaction
from app.wallets.model import Wallet
from app.merchants.model import Merchant
from app.models.user import User


def get_transactions(
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

    wallet = (
        db.query(Wallet)
        .filter(Wallet.merchant_id == merchant.id)
        .first()
    )

    if wallet is None:
        return None

    transactions = (
        db.query(Transaction)
        .filter(Transaction.wallet_id == wallet.id)
        .order_by(Transaction.created_at.desc())
        .all()
    )

    total_credits = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.type == "CREDIT",
            Transaction.status == "SUCCESS",
        )
        .scalar()
    )

    total_debits = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.type == "DEBIT",
            Transaction.status == "SUCCESS",
        )
        .scalar()
    )

    return {
        "wallet_balance": wallet.balance,
        "currency": wallet.currency,
        "total_credits": total_credits,
        "total_debits": total_debits,
        "transaction_count": len(transactions),
        "transactions": transactions,
    }