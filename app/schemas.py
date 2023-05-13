"""
This is where your data models will be defined
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    phone: str
    role: Optional[str] = "USER"

    class Config:
        orm_mode = True


class UserOut(User):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    phone: str
    password: str

    class Config:
        orm_mode = True


class Service(BaseModel):
    name: str
    description: str
    price: int
    address: str
    category: list = []

    class Config:
        orm_mode = True


class ServiceOut(Service):
    id: int
    created_at: datetime
    updated_at: datetime
    rating: float
    number_of_ratings: int
    user: UserOut

    class Config:
        orm_mode = True
