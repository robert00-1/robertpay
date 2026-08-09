from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TransactionResponse(BaseModel):
    id: int

    payment_id: int | None = None

    type: str
    amount: float
    balance_after: float

    reference: str
    description: str | None = None

    status: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionsDashboardResponse(BaseModel):
    wallet_balance: float
    currency: str

    total_credits: float
    total_debits: float
    transaction_count: int

    transactions: list[TransactionResponse]

    model_config = ConfigDict(from_attributes=True)