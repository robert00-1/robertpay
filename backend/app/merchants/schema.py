from pydantic import BaseModel, EmailStr
from datetime import datetime


class MerchantCreate(BaseModel):
    business_name: str
    business_email: EmailStr
    business_phone: str
    business_address: str | None = None
    kra_pin: str | None = None


class MerchantProfileUpdate(BaseModel):
    business_name: str | None = None
    business_email: EmailStr | None = None
    business_phone: str | None = None
    business_address: str | None = None
    owner_name: str | None = None
    business_type: str | None = None
    kra_pin: str | None = None
    paybill_number: str | None = None
    till_number: str | None = None


class MerchantResponse(BaseModel):
    id: int
    business_name: str
    business_email: EmailStr
    business_phone: str
    business_address: str | None = None
    owner_name: str | None = None
    business_type: str | None = None
    kra_pin: str | None = None
    till_number: str | None = None
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True