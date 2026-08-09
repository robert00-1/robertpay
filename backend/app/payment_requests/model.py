from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base

class PaymentRequest(Base):
    __tablename__ = "payment_requests"

    id = Column(Integer, primary_key=True, index=True)

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        nullable=False,
    )
    customer_name = Column(
        String(150),
        nullable=False,
    )

    customer_phone = Column(
        String(20),
        nullable=False,
    )
    customer_email = Column(
        String(255),
        nullable=True,
    )
    amount = Column(
        Float,
        nullable=False,
    )

    description = Column(
        String(255),
        nullable=True,
    )
    reference = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    status = Column(
        String(20),
        default="PENDING",
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    paid_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    merchant = relationship(
        "Merchant",
        back_populates="payment_requests"
    )
    payments = relationship(
        "Payment",
        back_populates="payment_request",
    )