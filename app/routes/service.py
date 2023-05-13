from fastapi import APIRouter, Depends, HTTPException
from ..database import get_db, SessionLocal
from ..models import ServiceModel
from typing import List
from http import HTTPStatus
from ..schemas import Service, UserOut, ServiceOut
from ..oauth2 import get_current_user


router = APIRouter(prefix="/services", tags=["service"])


@router.get("/", response_model=List[ServiceOut], status_code=HTTPStatus.OK.value)
async def getservices(
    db: SessionLocal = Depends(get_db),
    limit: int = 100,
    skip: int = 0,
    name: str = None,
):
    if name:
        return (
            db.query(ServiceModel)
            .filter(ServiceModel.name.ilike(f"%{name}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )
    return db.query(ServiceModel).offset(skip).limit(limit).all()


@router.get("/{service_id}", response_model=ServiceOut, status_code=HTTPStatus.OK.value)
async def getservice(service_id: int, db: SessionLocal = Depends(get_db)):
    searched_service = (
        db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
    )
    if searched_service is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"Service with id {service_id} not found",
        )
    return searched_service


@router.post("/", response_model=Service)
async def create_service(
    service: Service,
    db: SessionLocal = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    new_service = ServiceModel(user_id=current_user.id, **service.dict())

    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


@router.put("/{service_id}", response_model=Service)
async def update_service(
    service_id: int, service: Service, db: SessionLocal = Depends(get_db)
):
    service_to_update = (
        db.query(ServiceModel).filter(ServiceModel.id == service_id).update(service)
    )
    db.commit()
    if service_to_update is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"Service with id {service_id} not found",
        )

    return service


@router.delete("/{service_id}", response_model=Service)
async def delete_service(service_id: int, db: SessionLocal = Depends(get_db)):
    service_to_delete = (
        db.query(ServiceModel).filter(ServiceModel.id == service_id).delete()
    )
    db.commit()
    if service_to_delete is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"Service with id {service_id} not found",
        )

    return service_to_delete
