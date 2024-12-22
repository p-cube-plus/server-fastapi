from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.attendance import (
    AttendanceCreate,
    AttendanceDelete,
    AttendanceRead,
    AttendanceUpdate,
)
from app.service.attendance import AttendanceService

router = APIRouter(
    prefix="/attendance",
)


@router.get("", response_model=list[AttendanceRead])
async def get_attendance_list(service: Annotated[AttendanceService, Depends()]):
    attendance_list = await service.get_all()
    return attendance_list


@router.get("/{attendance_id}", response_model=AttendanceRead)
async def get_attendance_by_id(
    attendance_id: str, service: Annotated[AttendanceService, Depends()]
):
    attendance = await service.get_by_id(attendance_id)
    return attendance


@router.post("", response_model=AttendanceRead)
async def create_attendance(
    attendance: AttendanceCreate, service: Annotated[AttendanceService, Depends()]
):
    new_attendance = await service.create(attendance)
    return new_attendance


@router.put("", response_model=AttendanceRead)
async def update_attendance(
    attendance: AttendanceUpdate, service: Annotated[AttendanceService, Depends()]
):
    updated_attendance = await service.update(attendance)
    return updated_attendance


@router.delete("", response_model=AttendanceRead)
async def delete_attendance(
    attendance: AttendanceDelete, service: Annotated[AttendanceService, Depends()]
):
    deleted_attendance = await service.delete(attendance)
    return deleted_attendance
