from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RecentTransaction(BaseModel):
    id: int
    amount: float
    type: str
    status: str
    reference: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DashboardResponse(BaseModel):
    business_name: str
    wallet_balance: float
    currency: str

    is_verified: bool
    paybill_number: str | None = None
    till_number: str |None = None

    transaction_count: int

    successful_transactions: int
    failed_transactions: int
    pending_transactions: int

    today_revenue: float
    week_revenue: float
    month_revenue: float
    total_revenue: float

    recent_transactions: list[RecentTransaction]

    model_config = ConfigDict(from_attributes=True)