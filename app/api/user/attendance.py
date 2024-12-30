from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.attendance_member import (
    AttendanceMemberDTO,
    AttendanceMemberPost,
    UserAttendanceParams,
    UserAttendancePatch,
    UserAttendancePost,
    UserAttendancePut,
)
from app.service.attendance_member import AttendanceMemberService

router = CustomAPIRouter(
    prefix="/users/{user_id}/attendances",
)


@router.get("", response_model=list[AttendanceMemberDTO])
async def get_user_attendance_list(
    user_id: int,
    user_attendance_params: Annotated[UserAttendanceParams, Depends()],
    service: Annotated[AttendanceMemberService, Depends()],
):
    user_attendance_list = await service.get(
        user_id=user_id, **user_attendance_params.dict()
    )
    return user_attendance_list


@router.get("/{attendance_id}", response_model=AttendanceMemberDTO)
async def get_user_attendance_by_attendance_id(
    user_id: int,
    attendance_id: int,
    service: Annotated[AttendanceMemberService, Depends()],
):
    user_attendance = await service.get(user_id=user_id, attendance_id=attendance_id)
    return user_attendance[0]


@router.post("", response_model=AttendanceMemberDTO)
async def create_user_attendance(
    user_id: int,
    user_attendance_post: UserAttendancePost,
    service: Annotated[AttendanceMemberService, Depends()],
):
    new_user_attendance = await service.create(
        [AttendanceMemberPost(user_id=user_id, **user_attendance_post.dict())]
    )
    return new_user_attendance[0]


@router.put("/{attendance_id}", response_model=AttendanceMemberDTO)
async def update_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_put: UserAttendancePut,
    service: Annotated[AttendanceMemberService, Depends()],
):
    updated_user_attendance = await service.update(
        user_attendance_put,
        exclude_unset=False,
        user_id=user_id,
        attendance_id=attendance_id,
    )
    return updated_user_attendance[0]


@router.patch("/{attendance_id}", response_model=AttendanceMemberDTO)
async def patch_user_attendance(
    user_id: int,
    attendance_id: int,
    user_attendance_patch: UserAttendancePatch,
    service: Annotated[AttendanceMemberService, Depends()],
):
    patched_user_attendance = await service.update(
        user_attendance_patch, user_id=user_id, attendance_id=attendance_id
    )
    return patched_user_attendance[0]


@router.delete("/{attendance_id}", response_model=AttendanceMemberDTO)
async def delete_user_attendance(
    user_id: int,
    attendance_id: int,
    service: Annotated[AttendanceMemberService, Depends()],
):
    deleted_user_attendance = await service.delete(
        user_id=user_id, attendance_id=attendance_id
    )
    return deleted_user_attendance[0]
