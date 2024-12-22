from datetime import time

from .base import BaseDTO, Partial


class AttendanceID(BaseDTO):
    id: int


class AttendanceBase(BaseDTO):
    meeting_id: int
    first_auth_start_time: time = None
    first_auth_end_time: time = None
    second_auth_start_time: time = None
    second_auth_end_time: time = None


class AttendanceRequest(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase, AttendanceID):
    pass


class AttendancePayload(Partial(AttendanceBase)):
    pass
