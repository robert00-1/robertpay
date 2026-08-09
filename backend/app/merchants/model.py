from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Merchant(Base):
     __tablename__ = "merchants"

     id = Column(Integer, primary_key=True, index=True)

     business_name = Column(String(150), nullable=False)

     business_email = Column(String(255), unique=True, nullable=False)

     business_phone = Column(String(100) , nullable=False)

     business_address = Column(String(255), nullable=True)

     kra_pin = Column(String(30), nullable=True)
     
     owner_name = Column(
          String(150),
          nullable=True,
     )
     business_type = Column(
          String(100),
          nullable=True,
     )
     paybill_number = Column(
          String(20),
          nullable=True,
     )

     till_number = Column(
          String(20),
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
          String(255),
          nullable=True,
     )
     shortcode = Column(
          String(20),
          nullable=True,
     )

     callback_url = Column(
          String(255),
          nullable=True,
     )
     is_verified = Column(
          Boolean,
          default=False,
          nullable=False,
     )
     created_at = Column(
          DateTime(timezone=True),
          server_default=func.now(),
     )
     update_at = Column(
          DateTime(timezone=True),
          server_default=func.now(),
          onupdate=func.now(),
     )




     user_id = Column(
          Integer,
          ForeignKey("users.id"),
          nullable=False,
          unique=True
     )

     user = relationship(
          "User",
          back_populates="merchant"
          
          )
     
     wallet = relationship(
          "Wallet",
          back_populates="merchant",
          uselist=False,
     )

     api_key = relationship(
          "ApiKey",
          back_populates="merchant",
          uselist=False,
     )
     payments = relationship(
          "Payment",
          back_populates="merchant",
     )
     payment_requests = relationship(
          "PaymentRequest",
          back_populates="merchant",
     )
     settings = relationship(
          "MerchantSettings",
          back_populates="merchant",
          uselist=False,
     )

