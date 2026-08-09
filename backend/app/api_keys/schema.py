from pydantic import BaseModel
from datetime import datetime

class ApiKeyResponse(BaseModel):
    publishable_key: str
    secret_key: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True