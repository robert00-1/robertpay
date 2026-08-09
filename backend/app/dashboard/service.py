from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta

from app.models.user import User
from app.merchants.model import Merchant
from app.wallets.model import Wallet
from app.transactions.model import Transaction


def get_dashboard(
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

    today = date.today()
    week_start = today - timedelta(days=7)
    month_start = today.replace(day=1)

    # -------------------------
    # Transaction counts
    # -------------------------
    transaction_count = (
        db.query(Transaction)
        .filter(Transaction.wallet_id == wallet.id)
        .count()
    )

    successful_transactions = (
        db.query(Transaction)
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "SUCCESS",
        )
        .count()
    )

    failed_transactions = (
        db.query(Transaction)
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "FAILED",
        )
        .count()
    )

    pending_transactions = (
        db.query(Transaction)
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "PENDING",
        )
        .count()
    )

    # -------------------------
    # Revenue
    # -------------------------
    today_revenue = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "SUCCESS",
            func.date(Transaction.created_at) == today,
        )
        .scalar()
    )

    week_revenue = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "SUCCESS",
            func.date(Transaction.created_at) >= week_start,
        )
        .scalar()
    )

    month_revenue = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "SUCCESS",
            func.date(Transaction.created_at) >= month_start,
        )
        .scalar()
    )

    total_revenue = (
        db.query(func.coalesce(func.sum(Transaction.amount), 0))
        .filter(
            Transaction.wallet_id == wallet.id,
            Transaction.status == "SUCCESS",
        )
        .scalar()
    )

    # -------------------------
    # Recent Transactions
    # -------------------------
    recent_transactions = (
        db.query(Transaction)
        .filter(Transaction.wallet_id == wallet.id)
        .order_by(Transaction.created_at.desc())
        .limit(5)
        .all()
    )

    return {
        "business_name": merchant.business_name,
        "wallet_balance": wallet.balance,
        "currency": wallet.currency,

        "is_verified": merchant.is_verified,
        "paybill_number": merchant.paybill_number,
        "till_number": merchant.till_number,

        "transaction_count": transaction_count,

        "successful_transactions": successful_transactions,
        "failed_transactions": failed_transactions,
        "pending_transactions": pending_transactions,

        "today_revenue": today_revenue,
        "week_revenue": week_revenue,
        "month_revenue": month_revenue,
        "total_revenue": total_revenue,

        "recent_transactions": recent_transactions,
    }