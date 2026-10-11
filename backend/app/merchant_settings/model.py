from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base

class MerchantSettings(Base):
      __tablename__ = "merchant_settings"

      id = Column(
            Integer,
            primary_key=True,
            index=True,
            
      )
      merchant_id = Column(
            Integer,
            ForeignKey("merchants.id"),
            unique=True,
            nullable=False,
      )

      business_name = Column(
            String(255),
            nullable=False,
      )
      payment_type = Column(
            String(20),
            nullable=False,
            default="PAYBILL",
      )
      paybill_number = Column(
            String(20),
            nullable=True,
      )
      account_number = Column(
            String(100),
            nullable=True,
      )
      consumer_key = Column(
            String(255),
            nullable=True,
      )
      consumer_secret = Column(
            String(255),
            nullable=True,
      )
      passkey = Column(
            String(500),
            nullable=True,
      )
      callback_url = Column(
            String(500),
            nullable=True,
      )
      environment = Column("enviroment",
            String(20),
            default="SANDBOX",
      )
      is_active = Column(
            Boolean,
            default=True,
      )
      created_at = Column(
            DateTime(timezone=True),
            server_default=func.now(),
      )
      updated_at = Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
      )
      merchant = relationship(
            "Merchant",
            back_populates="settings",
      )
