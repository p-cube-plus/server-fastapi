from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.user import UserDTO, UserParams, UserPatch, UserPost, UserPut
from app.service.user import UserService

router = CustomAPIRouter(
    prefix="/users",
)


@router.get("", response_model=list[UserDTO])
async def get_user_list(
    user_params: Annotated[UserParams, Depends()],
    service: Annotated[UserService, Depends()],
):
    user_list = await service.get(**user_params.dict())
    return user_list


@router.get("/{id}", response_model=UserDTO)
async def get_user_by_id(id: int, service: Annotated[UserService, Depends()]):
    user_list = await service.get(id=id)
    if not user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user_list[0]


@router.post("", response_model=UserDTO)
async def create_user(user_post: UserPost, service: Annotated[UserService, Depends()]):
    new_user_list = await service.create([user_post])
    return new_user_list[0]


@router.put("/{id}", response_model=UserDTO)
async def replace_user(
    id: int, user_put: UserPut, service: Annotated[UserService, Depends()]
):
    replaced_user_list = await service.update(user_put, exclude_unset=False, id=id)
    if not replaced_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return replaced_user_list[0]


@router.patch("/{id}", response_model=UserDTO)
async def update_user(
    id: int, user_patch: UserPatch, service: Annotated[UserService, Depends()]
):
    updated_user_list = await service.update(user_patch, id=id)
    if not updated_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return updated_user_list[0]


@router.delete("/{id}", response_model=UserDTO)
async def delete_user(id: int, service: Annotated[UserService, Depends()]):
    deleted_user_list = await service.delete(id=id)
    if not deleted_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return deleted_user_list[0]
