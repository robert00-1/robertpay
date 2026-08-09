from typing import Optional

from pydantic import BaseModel, ConfigDict


class MerchantSettingsCreate(BaseModel):
    business_name: str
    payment_type: str = "PAYBILL"

    paybill_number: Optional[str] = None
    
    account_number: Optional[str] = None

    consumer_key: str
    consumer_secret: str
    passkey: str

    callback_url: Optional[str] = None
    environment: str = "SANDBOX"


class MerchantSettingsUpdate(BaseModel):
    business_name: Optional[str] = None
    payment_type: Optional[str] = None

    paybill_number: Optional[str] = None
    
    account_number: Optional[str] = None

    consumer_key: Optional[str] = None
    consumer_secret: Optional[str] = None
    passkey: Optional[str] = None

    callback_url: Optional[str] = None
    environment: Optional[str] = None

    is_active: Optional[bool] = None


class MerchantSettingsResponse(BaseModel):
    id: int
    merchant_id: int

    business_name: str
    payment_type: str

    paybill_number: Optional[str]
    
    account_number: Optional[str]

    consumer_key: Optional[str]
    consumer_secret: Optional[str]
    passkey: Optional[str]

    callback_url: Optional[str]
    environment: str

    is_active: bool

    model_config = ConfigDict(from_attributes=True)



 