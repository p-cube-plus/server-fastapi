from datetime import time
from typing import Optional

from .base import BaseDTO, Partial


class AttendanceMemberID(BaseDTO):
    id: int


class UserID(BaseDTO):
    user_id: int


class AttendanceID(BaseDTO):
    attendance_id: int


class AttendanceMemberBase(BaseDTO):
    state: int | None = None
    first_auth_time: time | None = None
    second_auth_time: time | None = None


class UserAttendanceRequest(AttendanceMemberBase, AttendanceID):
    pass


class AttendanceUserRequest(AttendanceMemberBase, UserID):
    pass


class AttendanceMemberRequest(AttendanceMemberBase, UserID, AttendanceID):
    pass


class AttendanceMemberResponse(
    AttendanceMemberBase, UserID, AttendanceID, AttendanceMemberID
):
    pass


class AttendanceMemberPayload(Partial(AttendanceMemberBase)):
    pass
