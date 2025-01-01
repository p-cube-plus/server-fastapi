from datetime import time
from typing import Optional

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class UserAttendanceID(BaseDTO):
    id: int


class UserAttendanceBase(BaseDTO):
    user_id: int
    attendance_id: int
    state: int | None = None
    first_auth_time: time | None = None
    second_auth_time: time | None = None


class UserAttendanceDTO(UserAttendanceBase, UserAttendanceID):
    pass


class UserAttendancePost(UserAttendanceBase):
    pass


class UserAttendancePut(UserAttendanceBase, UserAttendanceID):
    pass


class UserAttendancePatch(Partial(UserAttendanceBase)):
    pass


class UserAttendanceParams(Nullified(UserAttendanceBase), QueryParamsDTO):
    pass
