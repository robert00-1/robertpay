from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user
from app.models.user import User

from app.wallets.schema import WalletResponse, DepositRequest
from app.wallets.service import get_wallet, deposit_money

router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"],
)


@router.get("", response_model=WalletResponse)
def my_wallet(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    wallet = get_wallet(db, current_user)

    if wallet is None:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found",
        )

    return wallet


@router.post("/deposit", response_model=WalletResponse)
def deposit(
    payload: DepositRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    wallet = deposit_money(
        db,
        current_user,
        payload.amount,
    )

    return wallet