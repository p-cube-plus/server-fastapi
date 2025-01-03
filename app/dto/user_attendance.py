from datetime import time
from typing import Optional

from app.dto.attendance import AttendanceDTO
from app.dto.user import UserDTO

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class UserID(BaseDTO):
    user_id: int


class AttendanceID(BaseDTO):
    attendance_id: int


class UserAttendanceBase(BaseDTO):
    state: int | None = None
    first_auth_time: time | None = None
    second_auth_time: time | None = None


class UserAttendanceDTO(UserAttendanceBase, AttendanceID, UserID):
    pass


class UserAttendancePost(UserAttendanceBase, AttendanceID):
    pass


class UserAttendancePut(UserAttendanceBase):
    pass


class UserAttendancePatch(Partial(UserAttendanceBase)):
    pass


class UserAttendanceParams(Nullified(UserAttendanceBase), QueryParamsDTO):
    pass


class AttendanceUserPost(UserAttendanceBase, UserID):
    pass


class AttendanceUserPut(UserAttendanceBase):
    pass


class AttendanceUserPatch(Partial(UserAttendanceBase)):
    pass


class AttendanceUserParams(Nullified(UserAttendanceBase), QueryParamsDTO):
    pass


class UserAttendanceListDTO(BaseDTO):
    user_attendance: UserAttendanceDTO
    attendance: AttendanceDTO | None


class AttendanceUserListDTO(BaseDTO):
    user_attendance: UserAttendanceDTO
    user: UserDTO | None
