from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.user_attendance import (
    UserAttendanceDTO,
    UserAttendanceParams,
    UserAttendancePatch,
    UserAttendancePost,
    UserAttendancePut,
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
