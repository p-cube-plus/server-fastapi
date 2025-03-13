from dataclasses import Field
from datetime import date

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class AbsenceID(BaseDTO):
    id: int


class AbsenceBase(BaseDTO):
    user_id: int
    type: int  # 0: 재학, 1: 일반휴학, 2: 군휴학
    reason: str | None = None
    description: str | None = None
    expected_return_date: date | None = None


class AbsenceDTO(AbsenceBase, AbsenceID):
    pass


class AbsenceParam(Partial(AbsenceBase)):
    pass


class AbsencePost(AbsenceBase):
    pass


class AbsencePut(AbsenceBase):
    pass


class AbsencePatch(Partial(AbsenceBase)):
    pass


class AbsenceParams(Nullified(AbsenceBase), QueryParamsDTO):
    pass
