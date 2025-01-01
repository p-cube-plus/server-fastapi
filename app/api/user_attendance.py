from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.attendance import AttendanceDTO, AttendanceParams
from app.dto.user import UserDTO, UserParams
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


@router.post("", response_model=UserAttendanceDTO)
async def create_user_attendance(
    user_attendance_post: UserAttendancePost,
    service: Annotated[UserAttendanceService, Depends()],
):
    new_user_attendance = await service.create([user_attendance_post])
    return new_user_attendance[0]


@router.put("", response_model=UserAttendanceDTO)
async def replace_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_put: UserAttendancePut,
    service: Annotated[UserAttendanceService, Depends()],
):
    replaced_user_attendance = await service.update(
        user_attendance_put,
        exclude_unset=False,
        user_id=user_id,
        attendance_id=attendance_id,
    )
    return replaced_user_attendance[0]


@router.patch("", response_model=UserAttendanceDTO)
async def update_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_patch: UserAttendancePatch,
    service: Annotated[UserAttendanceService, Depends()],
):
    updated_user_attendance = await service.update(
        user_attendance_patch, user_id=user_id, attendance_id=attendance_id
    )
    return updated_user_attendance[0]


@router.delete("", response_model=UserAttendanceDTO)
async def delete_user_attendance(
    user_id: int,
    attendance_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    deleted_user_attendance = await service.delete(
        user_id=user_id, attendance_id=attendance_id
    )
    return deleted_user_attendance[0]


@router.get("/users/{user_id}", response_model=list[UserAttendanceRecordDTO])
async def get_user_attendance_records(
    user_id: int,
    attendance_params: Annotated[AttendanceParams, Depends()],
    service: Annotated[UserAttendanceService, Depends()],
):
    result = await service.get_user_attendance_records(
        user_id=user_id, **attendance_params.dict()
    )
    return [
        UserAttendanceRecordDTO(user_attendance=user_attendance, attendance=attendance)
        for user_attendance, attendance in result
    ]


@router.get(
    "/attendances/{attendance_id}", response_model=list[AttendanceUserRecordDTO]
)
async def get_attendance_user_records(
    attendance_id: int,
    user_params: Annotated[UserParams, Depends()],
    service: Annotated[UserAttendanceService, Depends()],
):
    result = await service.get_attendance_user_records(
        attendance_id=attendance_id, **user_params.dict()
    )
    return [
        AttendanceUserRecordDTO(user_attendance=user_attendance, user=user)
        for user_attendance, user in result
    ]
