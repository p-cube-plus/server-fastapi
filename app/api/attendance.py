from typing import Annotated

from fastapi import APIRouter, Depends

from app.dto.attendance import AttendanceCreate, AttendanceRead, AttendanceUpdate
from app.service.attendance import AttendanceService

router = APIRouter(
    prefix="/attendance",
)


@router.get("", response_model=list[AttendanceRead])
async def get_attendance_list(service: Annotated[AttendanceService, Depends()]):
    attendance_list = await service.get_all()
    return attendance_list


@router.get("/{id}", response_model=AttendanceRead)
async def get_attendance_by_id(
    id: int, service: Annotated[AttendanceService, Depends()]
):
    attendance = await service.get(id)
    return attendance


@router.post("", response_model=AttendanceRead)
async def create_attendance(
    attendance: AttendanceCreate, service: Annotated[AttendanceService, Depends()]
):
    new_attendance = await service.create(attendance)
    return new_attendance


@router.put("/{id}", response_model=AttendanceRead)
async def update_attendance(
    id: int,
    attendance: AttendanceUpdate,
    service: Annotated[AttendanceService, Depends()],
):
    updated_attendance = await service.update(id, attendance)
    return updated_attendance


@router.delete("/{id}", response_model=AttendanceRead)
async def delete_attendance(id: int, service: Annotated[AttendanceService, Depends()]):
    deleted_attendance = await service.delete(id)
    return deleted_attendance
