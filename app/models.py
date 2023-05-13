"""
This is where your database Tables will be defined
"""

from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
    role = Column(String(255), nullable=False, default="USER")
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"), onupdate=text("NOW()"))


class ServiceModel(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(
        "UserModel",
    )
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
    category = Column(ARRAY(String(255)), nullable=False)

    rating = Column(Integer, nullable=False, default=0)
    number_of_ratings = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True)
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"), onupdate=text("NOW()"))
