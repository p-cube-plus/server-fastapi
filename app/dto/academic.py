from dataclasses import Field

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class AcademicID(BaseDTO):
    id: int


class AcademicBase(BaseDTO):
    user_id: int
    university: str | None = None
    major: str | None = None
    grade: int
    student_id: str | None = None


class AcademicDTO(AcademicBase, AcademicID):
    pass


class AcademicParam(Partial(AcademicBase)):
    pass


class AcademicPost(AcademicBase):
    pass


class AcademicPut(AcademicBase):
    pass


class AcademicPatch(Partial(AcademicBase)):
    pass


class AcademicParams(Nullified(AcademicBase), QueryParamsDTO):
    pass
