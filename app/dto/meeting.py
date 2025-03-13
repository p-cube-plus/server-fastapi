from datetime import time

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


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


class MeetingPost(MeetingBase):
    pass


class MeetingPut(MeetingBase, MeetingID):
    pass


class MeetingPatch(Partial(MeetingBase)):
    pass


class MeetingParams(Nullified(MeetingBase), QueryParamsDTO):
    pass
