from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.attendance import (
    AttendanceDTO,
    AttendanceParams,
    AttendancePatch,
    AttendancePost,
    AttendancePut,
)
from app.service.attendance import AttendanceService

router = CustomAPIRouter(
    prefix="/attendances",
)


@router.get("", response_model=list[AttendanceDTO])
async def get_attendance_list(
    attendance_params: Annotated[AttendanceParams, Depends()],
    service: Annotated[AttendanceService, Depends()],
):
    attendance_list = await service.get(**attendance_params.dict())
    return attendance_list


@router.get("/{id}", response_model=AttendanceDTO)
async def get_attendance_by_id(
    id: int, service: Annotated[AttendanceService, Depends()]
):
    attendance_list = await service.get(id=id)
    if not attendance_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found"
        )
    return attendance_list[0]


@router.post("", response_model=AttendanceDTO)
async def create_attendance(
    attendance_post: AttendancePost,
    service: Annotated[AttendanceService, Depends()],
):
    new_attendance_list = await service.create([attendance_post])
    return new_attendance_list[0]


@router.put("/{id}", response_model=AttendanceDTO)
async def replace_attendance(
    id: int,
    attendance_put: AttendancePut,
    service: Annotated[AttendanceService, Depends()],
):
    replaced_attendance_list = await service.replace(attendance_put, id=id)
    if not replaced_attendance_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found"
        )
    return replaced_attendance_list[0]


@router.patch("/{id}", response_model=AttendanceDTO)
async def update_attendance(
    id: int,
    attendance_patch: AttendancePatch,
    service: Annotated[AttendanceService, Depends()],
):
    updated_attendance_list = await service.update(attendance_patch, id=id)
    if not updated_attendance_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found"
        )
    return updated_attendance_list[0]


@router.delete("/{id}", response_model=AttendanceDTO)
async def delete_attendance(id: int, service: Annotated[AttendanceService, Depends()]):
    deleted_attendance_list = await service.delete(id=id)
    if not deleted_attendance_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found"
        )
    return deleted_attendance_list[0]
