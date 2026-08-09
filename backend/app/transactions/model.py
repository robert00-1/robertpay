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

class Transaction(Base):
        __tablename__ = "transactions"


        id = Column(Integer, primary_key=True, index=True)

        wallet_id = Column(
                Integer,
                ForeignKey("wallets.id"),
                nullable=False,
        )

        payment_id = Column(
                Integer,
                ForeignKey("payments.id"),
                nullable=True,
        )

        type = Column(
                String(20),
                nullable=False,
        )

        amount = Column(
                Numeric(12, 2),
                nullable=False,

        )

        balance_after = Column(
                Numeric(12, 2),
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
                default="SUCCESS"
        )

        created_at = Column(
                DateTime(timezone=True),
                server_default=func.now(),
        )

        wallet = relationship(
                "Wallet",
                back_populates="transactions",
        )
        payment = relationship(
                "Payment",
                back_populates="transactions",
                
        )
