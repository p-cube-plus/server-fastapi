from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.user_attendance import (
    AttendanceUserParams,
    AttendanceUserPatch,
    AttendanceUserPost,
    AttendanceUserPut,
    UserAttendanceDTO,
)
from app.service.user_attendance import UserAttendanceService

router = CustomAPIRouter(
    prefix="/attendances/{attendance_id}/users",
)


@router.get("", response_model=list[UserAttendanceDTO])
async def get_attendance_user_list(
    attendance_id: int,
    attendance_user_params: Annotated[AttendanceUserParams, Depends()],
    service: Annotated[UserAttendanceService, Depends()],
):
    attendance_user_list = await service.get(
        attendance_id=attendance_id, **attendance_user_params.dict()
    )
    return attendance_user_list


@router.get("/{user_id}", response_model=UserAttendanceDTO)
async def get_attendance_user_by_user_id(
    attendance_id: int,
    user_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    attendance_user_list = await service.get(
        attendance_id=attendance_id, user_id=user_id
    )
    if not attendance_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance user not found"
        )
    return attendance_user_list[0]


@router.post("", response_model=UserAttendanceDTO)
async def create_attendance_user(
    attendance_id: int,
    attendance_user_post: AttendanceUserPost,
    service: Annotated[UserAttendanceService, Depends()],
):
    new_attendance_user_list = await service.create(
        [UserAttendanceDTO(attendance_id=attendance_id, **attendance_user_post.dict())]
    )
    return new_attendance_user_list[0]


@router.put("/{user_id}", response_model=UserAttendanceDTO)
async def update_attendance_user(
    attendance_id: int,
    user_id: int,
    attendance_user_put: AttendanceUserPut,
    service: Annotated[UserAttendanceService, Depends()],
):
    updated_attendance_user_list = await service.update(
        attendance_user_put,
        exclude_unset=False,
        attendance_id=attendance_id,
        user_id=user_id,
    )
    if not updated_attendance_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance user not found"
        )
    return updated_attendance_user_list[0]


@router.patch("/{user_id}", response_model=UserAttendanceDTO)
async def patch_attendance_user(
    attendance_id: int,
    user_id: int,
    attendance_user_patch: AttendanceUserPatch,
    service: Annotated[UserAttendanceService, Depends()],
):
    patched_attendance_user_list = await service.update(
        attendance_user_patch, attendance_id=attendance_id, user_id=user_id
    )
    if not patched_attendance_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance user not found"
        )
    return patched_attendance_user_list[0]


@router.delete("/{user_id}", response_model=UserAttendanceDTO)
async def delete_attendance_user(
    attendance_id: int,
    user_id: int,
    service: Annotated[UserAttendanceService, Depends()],
):
    deleted_attendance_user_list = await service.delete(
        attendance_id=attendance_id, user_id=user_id
    )
    if not deleted_attendance_user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Attendance user not found"
        )
    return deleted_attendance_user_list[0]
