from typing import Annotated

from fastapi import APIRouter, Depends

from app.dto.attendance import AttendanceResponse
from app.dto.attendance_member import (
    AttendanceMemberPayload,
    AttendanceMemberRequest,
    AttendanceMemberResponse,
    UserAttendanceRequest,
)
from app.service.attendance_member import AttendanceMemberService

router = APIRouter(
    prefix="/users/{user_id}/attendances",
)


@router.get("", response_model=list[AttendanceMemberResponse])
async def get_user_attendance_list(
    user_id: int, service: Annotated[AttendanceMemberService, Depends()]
):
    user_attendance = await service.get_all(AttendanceMemberPayload(user_id=user_id))
    return user_attendance


@router.get("/{attendance_id}", response_model=AttendanceMemberResponse)
async def get_user_attendance_by_attendance_id(
    user_id: int,
    attendance_id: int,
    service: Annotated[AttendanceMemberService, Depends()],
):
    user_attendance = await service.get_all(
        AttendanceMemberPayload(user_id=user_id, attendance_id=attendance_id)
    )
    if not user_attendance:
        return None
    return user_attendance[0]


@router.post("", response_model=AttendanceMemberResponse)
async def create_user_attendance(
    user_id: int,
    user_attendance_request: UserAttendanceRequest,
    service: Annotated[AttendanceMemberService, Depends()],
):
    new_user_attendance = await service.create(
        AttendanceMemberRequest(user_id=user_id, **user_attendance_request.dict())
    )
    return new_user_attendance
