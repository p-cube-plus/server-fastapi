from dataclasses import Field
from datetime import date

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class MembershipID(BaseDTO):
    id: int


class MembershipBase(BaseDTO):
    user_id: int
    level: int
    part: int
    join_date: date | None = None


class MembershipDTO(MembershipBase, MembershipID):
    pass


class MembershipParam(Partial(MembershipBase)):
    pass


class MembershipPost(MembershipBase):
    pass


class MembershipPut(MembershipBase):
    pass


class MembershipPatch(Partial(MembershipBase)):
    pass


class MembershipParams(Nullified(MembershipBase), QueryParamsDTO):
    pass
