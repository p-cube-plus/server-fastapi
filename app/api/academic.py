from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.academic import (
    AcademicDTO,
    AcademicParams,
    AcademicPatch,
    AcademicPost,
    AcademicPut,
)
from app.service.academic import AcademicService

router = CustomAPIRouter(
    prefix="/academics",
)


@router.get("", response_model=list[AcademicDTO])
async def get_academic_list(
    academic_params: Annotated[AcademicParams, Depends()],
    service: Annotated[AcademicService, Depends()],
):
    academic_list = await service.get(**academic_params.dict())
    return academic_list


@router.get("/{user_id}", response_model=AcademicDTO)
async def get_academic_by_user_id(
    user_id: int | str, service: Annotated[AcademicService, Depends()]
):
    academic_list = await service.get(user_id=user_id)
    if not academic_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Academic not found"
        )
    return academic_list[0]


@router.post("", response_model=AcademicDTO)
async def create_academic(
    academic_post: AcademicPost, service: Annotated[AcademicService, Depends()]
):
    new_academic_list = await service.create([academic_post])
    return new_academic_list[0]


@router.put("/{user_id}", response_model=AcademicDTO)
async def replace_academic(
    user_id: int | str,
    academic_put: AcademicPut,
    service: Annotated[AcademicService, Depends()],
):
    replaced_academic_list = await service.update(
        academic_put, exclude_unset=False, user_id=user_id
    )
    if not replaced_academic_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Academic not found"
        )
    return replaced_academic_list[0]


@router.patch("/{user_id}", response_model=AcademicDTO)
async def update_academic(
    user_id: int | str,
    academic_patch: AcademicPatch,
    service: Annotated[AcademicService, Depends()],
):
    updated_academic_list = await service.update(academic_patch, user_id=user_id)
    if not updated_academic_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Academic not found"
        )
    return updated_academic_list[0]


@router.delete("/{user_id}", response_model=AcademicDTO)
async def delete_academic(
    user_id: int | str, service: Annotated[AcademicService, Depends()]
):
    deleted_academic_list = await service.delete(user_id=user_id)
    if not deleted_academic_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Academic not found"
        )
    return deleted_academic_list[0]
