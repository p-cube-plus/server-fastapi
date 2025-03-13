from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.profile import (
    ProfileDTO,
    ProfileParams,
    ProfilePatch,
    ProfilePost,
    ProfilePut,
)
from app.service.profile import ProfileService

router = CustomAPIRouter(
    prefix="/profiles",
)


@router.get("", response_model=list[ProfileDTO])
async def get_profile_list(
    profile_params: Annotated[ProfileParams, Depends()],
    service: Annotated[ProfileService, Depends()],
):
    profile_list = await service.get(**profile_params.dict())
    return profile_list


@router.get("/{user_id}", response_model=ProfileDTO)
async def get_profile_by_user_id(
    user_id: int, service: Annotated[ProfileService, Depends()]
):
    profile_list = await service.get(user_id=user_id)
    if not profile_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )
    return profile_list[0]


@router.post("", response_model=ProfileDTO)
async def create_profile(
    profile_post: ProfilePost, service: Annotated[ProfileService, Depends()]
):
    new_profile_list = await service.create([profile_post])
    return new_profile_list[0]


@router.put("/{user_id}", response_model=ProfileDTO)
async def replace_profile(
    user_id: int,
    profile_put: ProfilePut,
    service: Annotated[ProfileService, Depends()],
):
    replaced_profile_list = await service.update(
        profile_put, exclude_unset=False, user_id=user_id
    )
    if not replaced_profile_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )
    return replaced_profile_list[0]


@router.patch("/{user_id}", response_model=ProfileDTO)
async def update_profile(
    user_id: int,
    profile_patch: ProfilePatch,
    service: Annotated[ProfileService, Depends()],
):
    updated_profile_list = await service.update(profile_patch, user_id=user_id)
    if not updated_profile_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )
    return updated_profile_list[0]


@router.delete("/{user_id}", response_model=ProfileDTO)
async def delete_profile(user_id: int, service: Annotated[ProfileService, Depends()]):
    deleted_profile_list = await service.delete(user_id=user_id)
    if not deleted_profile_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found"
        )
    return deleted_profile_list[0]
