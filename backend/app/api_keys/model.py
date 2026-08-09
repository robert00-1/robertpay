from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)


    merchant_id =Column(
        Integer,
        ForeignKey("merchants.id"),
        unique=True,
        nullable=False,
    )

    publishable_key = Column(
        String(255),
        unique=True,
        nullable=False,
    )
    secret_key = Column(
        String(255),
        unique=True,
        nullable=False,
    )
    environment = Column(
        String(20),
        default="SANDBOX",
    )
    status = Column(
        String(20),
        default="ACTIVE",
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    merchant = relationship(
        "Merchant",
        back_populates="api_key",
    )