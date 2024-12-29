from typing import Annotated

from fastapi import APIRouter, Depends

from app.dto.attendance_member import (
    AttendanceMemberBase,
    AttendanceMemberDTO,
    AttendanceMemberPost,
    UserAttendancePost,
)
from app.service.attendance_member import AttendanceMemberService

router = APIRouter(
    prefix="/users/{user_id}/attendances",
)


@router.get("", response_model=list[AttendanceMemberDTO])
async def get_user_attendance_list(
    user_id: int, service: Annotated[AttendanceMemberService, Depends()]
):
    user_attendance_list = await service.get(user_id=user_id)
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
