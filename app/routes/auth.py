from fastapi import APIRouter, Depends, HTTPException, Body
from http import HTTPStatus

from ..database import get_db, SessionLocal
from ..models import UserModel
from typing import List

from ..schemas import Token
from ..utils import verify, hash
from ..oauth2 import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token, status_code=HTTPStatus.OK.value)
def login(
    user: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)
):
    credentials = db.query(UserModel).filter(UserModel.phone == user.username).first()
    print(credentials)

    if credentials is None:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Incorrect username or password"
        )

    if verify(user.password, credentials.password):
        return create_access_token(data={"user_id": credentials.id})

    else:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Incorrect username or password"
        )
