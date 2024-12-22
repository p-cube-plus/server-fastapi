from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.user import UserCreate, UserRead, UserUpdate
from app.service.user import UserService

router = APIRouter(
    prefix="/user",
)


@router.get("", response_model=list[UserRead])
async def get_user_list(service: Annotated[UserService, Depends()]):
    user_list = await service.get_all()
    return user_list


@router.get("/{id}", response_model=UserRead)
async def get_user_by_id(id: str, service: Annotated[UserService, Depends()]):
    user = await service.get(id)
    return user


@router.post("", response_model=UserRead)
async def create_user(user: UserCreate, service: Annotated[UserService, Depends()]):
    new_user = await service.create(user)
    return new_user


@router.put("/{id}", response_model=UserRead)
async def update_user(
    id: str, user: UserUpdate, service: Annotated[UserService, Depends()]
):
    updated_user = await service.update(id, user)
    return updated_user


@router.delete("/{id}", response_model=UserRead)
async def delete_user(id: str, service: Annotated[UserService, Depends()]):
    deleted_user = await service.delete(id)
    return deleted_user
