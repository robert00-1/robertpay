from decimal import Decimal
from pydantic import BaseModel, Field
from datetime import datetime

class DepositRequest(BaseModel):
    amount: Decimal = Field(..., gt=0)

class WalletResponse(BaseModel):
    id: int
    balance: Decimal
    currency: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True