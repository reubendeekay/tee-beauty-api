'''
This is where your data models will be defined
'''
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):

    name: str
    phone: str


class UserOut(User):

    id: int
    created_at: datetime
    updated_at: datetime
