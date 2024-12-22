from datetime import time

from .base import BaseDTO, Partial


class MeetingID(BaseDTO):
    id: int


class MeetingBase(BaseDTO):
    type: int
    title: str
    location: str
    day: int
    time: time


class MeetingRequest(MeetingBase):
    pass


class MeetingResponse(MeetingBase, MeetingID):
    pass


class MeetingPayload(Partial(MeetingBase)):
    pass
