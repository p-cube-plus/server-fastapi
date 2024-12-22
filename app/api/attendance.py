from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.dto.attendance import AttendancePayload, AttendanceRequest, AttendanceResponse
from app.service.attendance import AttendanceService

router = APIRouter(
    prefix="/attendances",
)


@router.get("", response_model=list[AttendanceResponse])
async def get_attendance_list(
    request: Request, service: Annotated[AttendanceService, Depends()]
):
    attendance_list = await service.get_all(AttendancePayload(**request.query_params))
    return attendance_list


@router.get("/{id}", response_model=AttendanceResponse)
async def get_attendance_by_id(
    id: int, service: Annotated[AttendanceService, Depends()]
):
    attendance = await service.get(id)
    return attendance


@router.post("", response_model=AttendanceResponse)
async def create_attendance(
    attendance: AttendanceRequest, service: Annotated[AttendanceService, Depends()]
):
    new_attendance = await service.create(attendance)
    return new_attendance


@router.put("/{id}", response_model=AttendanceResponse)
async def update_attendance(
    id: int,
    attendance: AttendancePayload,
    service: Annotated[AttendanceService, Depends()],
):
    updated_attendance = await service.update(id, attendance)
    return updated_attendance


@router.delete("/{id}", response_model=AttendanceResponse)
async def delete_attendance(id: int, service: Annotated[AttendanceService, Depends()]):
    deleted_attendance = await service.delete(id)
    return deleted_attendance
