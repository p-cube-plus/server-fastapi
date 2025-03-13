from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.absence import (
    AbsenceDTO,
    AbsenceParams,
    AbsencePatch,
    AbsencePost,
    AbsencePut,
)
from app.service.absence import AbsenceService

router = CustomAPIRouter(
    prefix="/absences",
)


@router.get("", response_model=list[AbsenceDTO])
async def get_absence_list(
    absence_params: Annotated[AbsenceParams, Depends()],
    service: Annotated[AbsenceService, Depends()],
):
    absence_list = await service.get(**absence_params.dict())
    return absence_list


@router.get("/{user_id}", response_model=AbsenceDTO)
async def get_absence_by_user_id(
    user_id: int, service: Annotated[AbsenceService, Depends()]
):
    absence_list = await service.get(user_id=user_id)
    if not absence_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Absence not found"
        )
    return absence_list[0]


@router.post("", response_model=AbsenceDTO)
async def create_absence(
    absence_post: AbsencePost, service: Annotated[AbsenceService, Depends()]
):
    new_absence_list = await service.create([absence_post])
    return new_absence_list[0]


@router.put("/{user_id}", response_model=AbsenceDTO)
async def replace_absence(
    user_id: int,
    absence_put: AbsencePut,
    service: Annotated[AbsenceService, Depends()],
):
    replaced_absence_list = await service.update(
        absence_put, exclude_unset=False, user_id=user_id
    )
    if not replaced_absence_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Absence not found"
        )
    return replaced_absence_list[0]


@router.patch("/{user_id}", response_model=AbsenceDTO)
async def update_absence(
    user_id: int,
    absence_patch: AbsencePatch,
    service: Annotated[AbsenceService, Depends()],
):
    updated_absence_list = await service.update(absence_patch, user_id=user_id)
    if not updated_absence_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Absence not found"
        )
    return updated_absence_list[0]


@router.delete("/{user_id}", response_model=AbsenceDTO)
async def delete_absence(user_id: int, service: Annotated[AbsenceService, Depends()]):
    deleted_absence_list = await service.delete(user_id=user_id)
    if not deleted_absence_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Absence not found"
        )
    return deleted_absence_list[0]
