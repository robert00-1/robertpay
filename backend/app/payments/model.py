from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base

class Payment(Base):
     __tablename__ = "payments"

     id = Column(Integer, primary_key=True, index=True)

     merchant_id = Column(
          Integer,
          ForeignKey("merchants.id"),
          nullable=False,
     )
     amount = Column(
          Numeric(12, 2),
          nullable=False,
     )
     phone_number = Column(
          String(20),
          nullable=False,
     )
     reference = Column(
          String(100),
          unique=True,
          nullable=False,
     )
     description = Column(
          String(255),
          nullable=True,
     )
     status = Column(
          String(20),
          default="PENDING",
     )
     checkout_request_id = Column(
          String(100),
          nullable=True
     )
     merchant_request_id = Column(
          String(100),
          nullable=True,
     )
     mpesa_receipt_number = Column(
          String(100),
          nullable=True,
     )
     result_code = Column(
          Integer,
          nullable=True,
     )
     result_desc = Column(
          String(255),
          nullable=True,
     )
     paid_at = Column(
          DateTime(timezone=True),
          nullable=True,
     )
     payment_request_id = Column(
          Integer,
          ForeignKey("payment_requests.id"),
          nullable=True,
     )

     created_at = Column(
          DateTime(timezone=True),
          server_default=func.now(),
          
     )
     merchant = relationship(
          "Merchant",
          back_populates="payments",
     )
     transactions = relationship(
          "Transaction",
          back_populates="payment",
          
     )
     payment_request = relationship(
          "PaymentRequest",
          back_populates="payments",
     )
