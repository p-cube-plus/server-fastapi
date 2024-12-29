from datetime import time
from typing import Optional

from .base import BaseDTO, Nullified, Partial


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


class AttendanceMemberDTO(
    AttendanceMemberBase, UserID, AttendanceID, AttendanceMemberID
):
    pass


class AttendanceMemberPost(AttendanceMemberBase, UserID, AttendanceID):
    pass


class UserAttendancePost(AttendanceMemberBase, AttendanceID):
    pass


class UserAttendancePut(AttendanceMemberBase):
    pass


class UserAttendancePatch(Partial(AttendanceMemberBase)):
    pass


class UserAttendanceParams(Nullified(AttendanceMemberBase)):
    pass


class AttendanceUserPost(AttendanceMemberBase, UserID):
    pass


class AttendanceUserPut(AttendanceMemberBase):
    pass


class AttendanceUserPatch(Partial(AttendanceMemberBase)):
    pass


class AttendanceUserParams(Nullified(AttendanceMemberBase)):
    pass
