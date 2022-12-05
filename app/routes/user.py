'''
This is a dummy route that will be used to define the users endpoint

'''


from fastapi import APIRouter, Depends
from ..database import get_db, SessionLocal
from ..models import UserModel


router = APIRouter(prefix='/users', tags=['user'])


@router.get('/')
async def get_users(db: SessionLocal = Depends(get_db)):
    return db.query(UserModel).all()
