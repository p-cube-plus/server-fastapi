from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.dto.attendance import (
    AttendanceDTO,
    AttendanceParams,
    AttendancePatch,
    AttendancePost,
    AttendancePut,
)
from app.service.attendance import AttendanceService

router = APIRouter(
    prefix="/attendances",
)


@router.get("", response_model=list[AttendanceDTO])
async def get_attendance_list(
    request: Request,
    attendance_params: Annotated[AttendanceParams, Depends()],
    service: Annotated[AttendanceService, Depends()],
):
    attendance_list = await service.get(**request.query_params)
    return attendance_list


@router.get("/{id}", response_model=AttendanceDTO)
async def get_attendance_by_id(
    id: int, service: Annotated[AttendanceService, Depends()]
):
    attendance = await service.get(id=id)
    return attendance[0]


@router.post("", response_model=AttendanceDTO)
async def create_attendance(
    attendance_post: AttendancePost,
    service: Annotated[AttendanceService, Depends()],
):
    new_attendance = await service.create([attendance_post])
    return new_attendance[0]


@router.put("/{id}", response_model=AttendanceDTO)
async def replace_attendance(
    id: int,
    attendance_put: AttendancePut,
    service: Annotated[AttendanceService, Depends()],
):
    replaced_attendance = await service.replace(attendance_put, id=id)
    return replaced_attendance[0]


@router.patch("/{id}", response_model=AttendanceDTO)
async def update_attendance(
    id: int,
    attendance_patch: AttendancePatch,
    service: Annotated[AttendanceService, Depends()],
):
    updated_attendance = await service.update(attendance_patch, id=id)
    return updated_attendance[0]


@router.delete("/{id}", response_model=AttendanceDTO)
async def delete_attendance(id: int, service: Annotated[AttendanceService, Depends()]):
    deleted_attendance = await service.delete(id=id)
    return deleted_attendance[0]
