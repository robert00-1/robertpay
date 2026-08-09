from datetime import datetime
from pydantic import BaseModel, EmailStr


class PaymentRequestCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: EmailStr | None = None

    amount: float
    description: str | None = None

    # Every payment request should have a unique reference
    reference: str


class PaymentRequestResponse(BaseModel):
    id: int

    customer_name: str
    customer_phone: str
    customer_email: EmailStr | None = None

    amount: float
    description: str | None = None

    reference: str
    status: str

    created_at: datetime
    paid_at: datetime | None = None

    class Config:
        from_attributes = True