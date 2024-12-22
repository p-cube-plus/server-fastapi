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


class MeetingCreate(MeetingBase):
    pass


class MeetingRead(MeetingBase, MeetingID):
    pass


class MeetingUpdate(Partial(MeetingBase), MeetingID):
    pass


class MeetingDelete(MeetingID):
    pass
