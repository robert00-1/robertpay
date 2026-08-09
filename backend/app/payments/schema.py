from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel


class PaymentCreate(BaseModel):
    amount: Decimal
    phone_number: str
    reference: str
    description: str | None = None


class PaymentResponse(BaseModel):
    id: int
    amount: Decimal
    phone_number: str
    reference: str
    description: str | None = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True