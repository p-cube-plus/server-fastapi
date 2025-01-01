from datetime import date, time

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class AttendanceID(BaseDTO):
    id: int


class AttendanceBase(BaseDTO):
    meeting_id: int
    date: date
    first_auth_start_time: time = None
    first_auth_end_time: time = None
    second_auth_start_time: time = None
    second_auth_end_time: time = None


class AttendanceDTO(AttendanceBase, AttendanceID):
    pass


class AttendancePost(AttendanceBase):
    pass


class AttendancePut(AttendanceBase):
    pass


class AttendancePatch(Partial(AttendanceBase)):
    pass


class AttendanceParams(Nullified(AttendanceBase), QueryParamsDTO):
    pass
