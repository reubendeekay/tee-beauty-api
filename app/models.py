'''
This is where your database Tables will be defined
'''

from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP, server_default=text(
        'NOW()'), onupdate=text('NOW()'))
