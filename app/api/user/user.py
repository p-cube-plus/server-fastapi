from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.dto.user import UserPayload, UserRequest, UserResponse
from app.service.user import UserService

router = APIRouter(
    prefix="/users",
)


@router.get("", response_model=list[UserResponse])
async def get_user_list(
    request: Request,
    user_payload: Annotated[UserPayload, Depends()],
    service: Annotated[UserService, Depends()],
):
    user_list = await service.get_all(UserPayload(**request.query_params))
    return user_list


@router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: int, service: Annotated[UserService, Depends()]):
    user = await service.get(id)
    return user


@router.post("", response_model=UserResponse)
async def create_user(
    user_request: UserRequest, service: Annotated[UserService, Depends()]
):
    new_user = await service.create(user_request)
    return new_user


@router.put("/{id}", response_model=UserResponse)
async def update_user(
    id: int, user_payload: UserPayload, service: Annotated[UserService, Depends()]
):
    updated_user = await service.update(id, user_payload)
    return updated_user


@router.delete("/{id}", response_model=UserResponse)
async def delete_user(id: int, service: Annotated[UserService, Depends()]):
    deleted_user = await service.delete(id)
    return deleted_user
