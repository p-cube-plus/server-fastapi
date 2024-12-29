from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.dto.user import UserDTO, UserParams, UserPatch, UserPost, UserPut
from app.service.user import UserService

router = APIRouter(
    prefix="/users",
)


@router.get("", response_model=list[UserDTO])
async def get_user_list(
    request: Request,
    user_params: Annotated[UserParams, Depends()],
    service: Annotated[UserService, Depends()],
):
    user_list = await service.get(**request.query_params)
    return user_list


@router.get("/{id}", response_model=UserDTO)
async def get_user_by_id(id: int, service: Annotated[UserService, Depends()]):
    user = await service.get(id=id)
    return user[0]


@router.post("", response_model=UserDTO)
async def create_user(user_post: UserPost, service: Annotated[UserService, Depends()]):
    new_user = await service.create([user_post])
    return new_user[0]


@router.put("/{id}", response_model=UserDTO)
async def replace_user(
    id: int, user_put: UserPut, service: Annotated[UserService, Depends()]
):
    replaced_user = await service.update(user_put, exclude_unset=False, id=id)
    return replaced_user[0]


@router.patch("/{id}", response_model=UserDTO)
async def update_user(
    id: int, user_patch: UserPatch, service: Annotated[UserService, Depends()]
):
    updated_user = await service.update(user_patch, id=id)
    return updated_user[0]


@router.delete("/{id}", response_model=UserDTO)
async def delete_user(id: int, service: Annotated[UserService, Depends()]):
    deleted_user = await service.delete(id=id)
    return deleted_user[0]
