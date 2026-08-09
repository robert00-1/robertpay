from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)

    balance = Column(Numeric(12, 2), default=0)

    currency = Column(String(10), default="KES")

    status = Column(String(20), default="ACTIVE")

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        unique=True,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    merchant = relationship(
        "Merchant",
        back_populates="wallet",
    )
    transactions = relationship(
        "Transaction",
        back_populates="wallet",
        cascade="all, delete-orphan",
    )