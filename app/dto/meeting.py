from datetime import time

from .base import BaseDTO, Nullified, Partial


class MeetingID(BaseDTO):
    id: int


class MeetingBase(BaseDTO):
    type: int
    title: str
    location: str
    day: int
    time: time


class MeetingDTO(MeetingBase, MeetingID):
    pass


class MeetigPost(MeetingBase):
    pass


class MeetingPut(MeetingBase, MeetingID):
    pass


class MeetingPatch(Partial(MeetingBase)):
    pass


class MeetingParams(Nullified(MeetingBase)):
    pass
