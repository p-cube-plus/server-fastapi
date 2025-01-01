from datetime import datetime
from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.attendance import AttendanceParams, AttendancePost
from app.dto.user_attendance import (
    UserAttendanceDTO,
    UserAttendanceListDTO,
    UserAttendanceParams,
    UserAttendancePatch,
    UserAttendancePost,
    UserAttendancePut,
)
from app.service.attendance import AttendanceService
from app.service.user_attendance import UserAttendanceService

router = CustomAPIRouter(
    prefix="/users/{user_id}/attendances",
)


@router.get("", response_model=list[UserAttendanceDTO])
async def get_user_attendance_list(
    user_id: int,
    user_attendance_params: Annotated[UserAttendanceParams, Depends()],
    service: Annotated[UserAttendanceService, Depends()],
):
    user_attendance_list = await service.get(
        user_id=user_id, **user_attendance_params.dict()
    )
    return user_attendance_list


@router.get("/today", response_model=list[UserAttendanceListDTO])
async def get_user_attendance_records(
    user_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    today = datetime.now().date()

    result = await service.get_user_attendance_list(user_id=user_id, date=today)
    return [
        UserAttendanceListDTO(user_attendance=user_attendance, attendance=attendance)
        for user_attendance, attendance in result
    ]


@router.get("/{attendance_id}", response_model=UserAttendanceDTO)
async def get_user_attendance_by_attendance_id(
    user_id: int,
    attendance_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    user_attendance = await service.get(user_id=user_id, attendance_id=attendance_id)
    return user_attendance[0]


@router.post("", response_model=UserAttendanceDTO)
async def create_user_attendance(
    user_id: int,
    user_attendance_post: UserAttendancePost,
    service: Annotated[UserAttendanceService, Depends()],
):
    new_user_attendance = await service.create(
        [UserAttendanceDTO(user_id=user_id, **user_attendance_post.dict())]
    )
    return new_user_attendance[0]


@router.put("/{attendance_id}", response_model=UserAttendanceDTO)
async def update_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_put: UserAttendancePut,
    service: Annotated[UserAttendanceService, Depends()],
):
    updated_user_attendance = await service.update(
        user_attendance_put,
        exclude_unset=False,
        user_id=user_id,
        attendance_id=attendance_id,
    )
    return updated_user_attendance[0]


@router.patch("/{attendance_id}", response_model=UserAttendanceDTO)
async def patch_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_patch: UserAttendancePatch,
    service: Annotated[UserAttendanceService, Depends()],
):
    patched_user_attendance = await service.update(
        user_attendance_patch, user_id=user_id, attendance_id=attendance_id
    )
    return patched_user_attendance[0]


@router.delete("/{attendance_id}", response_model=UserAttendanceDTO)
async def delete_user_attendance(
    user_id: int,
    attendance_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    deleted_user_attendance = await service.delete(
        user_id=user_id, attendance_id=attendance_id
    )
    return deleted_user_attendance[0]


@router.patch("/{attendance_id}/request", response_model=UserAttendanceDTO)
async def request_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_service: Annotated[UserAttendanceService, Depends()],
):
    current_datetime = datetime.now()
    requested_user_attendance = await user_attendance_service.request_user_attendance(
        user_id=user_id, attendance_id=attendance_id, current_datetime=current_datetime
    )
    return requested_user_attendance
