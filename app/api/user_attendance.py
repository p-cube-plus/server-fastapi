from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.attendance import AttendanceDTO
from app.dto.user import UserDTO
from app.dto.user_attendance import (
    AttendanceUserRecordDTO,
    UserAttendanceDTO,
    UserAttendanceParams,
    UserAttendancePatch,
    UserAttendancePost,
    UserAttendancePut,
    UserAttendanceRecordDTO,
)
from app.service.user_attendance import UserAttendanceService

router = CustomAPIRouter(
    prefix="/user_attendances",
)


@router.get("", response_model=list[UserAttendanceDTO])
async def get_user_attendance_list(
    user_attendance_params: Annotated[UserAttendanceParams, Depends()],
    service: Annotated[UserAttendanceService, Depends()],
):
    user_attendance_list = await service.get(**user_attendance_params.dict())
    return user_attendance_list


@router.get("/{id}", response_model=UserAttendanceDTO)
async def get_user_attendance_by_id(
    id: int, service: Annotated[UserAttendanceService, Depends()]
):
    user_attendance = await service.get(id=id)
    return user_attendance[0]


@router.post("", response_model=UserAttendanceDTO)
async def create_user_attendance(
    user_attendance_post: UserAttendancePost,
    service: Annotated[UserAttendanceService, Depends()],
):
    new_user_attendance = await service.create([user_attendance_post])
    return new_user_attendance[0]


@router.put("/{id}", response_model=UserAttendanceDTO)
async def replace_user_attendance(
    id: int,
    user_attendance_put: UserAttendancePut,
    service: Annotated[UserAttendanceService, Depends()],
):
    replaced_user_attendance = await service.replace(user_attendance_put, id=id)
    return replaced_user_attendance[0]


@router.patch("/{id}", response_model=UserAttendanceDTO)
async def update_user_attendance(
    id: int,
    user_attendance_patch: UserAttendancePatch,
    service: Annotated[UserAttendanceService, Depends()],
):
    updated_user_attendance = await service.update(user_attendance_patch, id=id)
    return updated_user_attendance[0]


@router.delete("/{id}", response_model=UserAttendanceDTO)
async def delete_user_attendance(
    id: int, service: Annotated[UserAttendanceService, Depends()]
):
    deleted_user_attendance = await service.delete(id=id)
    return deleted_user_attendance[0]


@router.get("/users/{user_id}", response_model=list[UserAttendanceRecordDTO])
async def get_user_attendance_records(
    user_id: int, service: Annotated[UserAttendanceService, Depends()]
):
    result = await service.get_user_attendance_records(user_id=user_id)
    return [
        UserAttendanceRecordDTO(user_attendance=user_attendance, attendance=attendance)
        for user_attendance, attendance in result
    ]


@router.get(
    "/attendances/{attendance_id}", response_model=list[AttendanceUserRecordDTO]
)
async def get_attendance_user_records(
    attendance_id: int, service: Annotated[UserAttendanceService, Depends()]
):
    result = await service.get_attendance_user_records(attendance_id=attendance_id)
    return [
        AttendanceUserRecordDTO(user_attendance=user_attendance, user=user)
        for user_attendance, user in result
    ]
