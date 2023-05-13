from fastapi import APIRouter, Depends, HTTPException, Body
from http import HTTPStatus

from ..database import get_db, SessionLocal
from ..models import UserModel
from typing import List

from ..schemas import UserCreate, UserOut
from ..utils import hash


router = APIRouter(prefix="/users", tags=["user"])


@router.get("/", response_model=List[UserOut], status_code=HTTPStatus.OK.value)
async def get_users(
    db: SessionLocal = Depends(get_db),
    limit: int = 100,
    skip: int = 0,
    name: str = None,
):
    if name:
        return (
            db.query(UserModel)
            .filter(UserModel.name.ilike(f"%{name}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )
    return db.query(UserModel).offset(skip).limit(limit).all()


@router.get("/{user_id}", response_model=UserOut, status_code=HTTPStatus.OK.value)
async def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    searched_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if searched_user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"User with id {user_id} not found",
        )
    return searched_user


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    user.password = hash(user.password)
    db_user = db.query(UserModel).filter(UserModel.phone == user.phone).first()
    if db_user is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail=f"User with phone {user.phone} already exists",
        )
    new_user = UserModel(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put("/{user_id}", response_model=UserCreate)
async def update_user(
    user_id: int, user: UserCreate, db: SessionLocal = Depends(get_db)
):
    user_to_update = db.query(UserModel).filter(UserModel.id == user_id).update(user)
    db.commit()
    if user_to_update is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"User with id {user_id} not found",
        )

    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: SessionLocal = Depends(get_db)):
    db.query(UserModel).filter(UserModel.id == user_id).delete()
    db.commit()
    return {"message": "User deleted successfully"}
