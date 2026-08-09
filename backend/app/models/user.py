from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__= "users"
    
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    phone = Column(String(20), unique=True, nullable=False)

    password= Column(String(255), nullable=False)

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    merchant = relationship(
        "Merchant",
        back_populates="user",
        uselist=False
    )