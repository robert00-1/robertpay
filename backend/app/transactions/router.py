from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.transactions.service import get_transactions
from app.transactions.schema import TransactionsDashboardResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.get(
    "",
    response_model=TransactionsDashboardResponse,
)
def transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = get_transactions(
        db,
        current_user,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found",
        )

    return result