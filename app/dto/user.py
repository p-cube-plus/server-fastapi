from dataclasses import Field
from datetime import date

from .base import BaseDTO, Nullified, Partial


class UserID(BaseDTO):
    id: int


class UserBase(BaseDTO):
    hash: str
    is_signed: bool = False
    name: str
    level: int
    grade: int
    part_index: int
    profile_image: str | None = None
    univ: str | None = None
    last_cleaning: date | None = None
    rest_type: int
    etc_message: str | None = None
    absent_reason: str | None = None
    absent_detail_reason: str | None = None
    phone_number: str | None = None
    join_date: date | None = None
    birth_date: date | None = None
    birth_month: int | None = None
    birth_day: int | None = None
    major: str | None = None
    student_id: str | None = None
    is_next_birth: bool = False
    return_plan_date: date | None = None
    workshop_count: int | None = None
    gogoma: str | None = None
    warning_point: int = 0
    fcm_token: str | None = None
    api_access_level: int = 0


class UserDTO(UserBase, UserID):
    pass


class UserParam(Partial(UserBase)):
    pass


class UserPost(UserBase):
    pass


class UserPut(UserBase):
    pass


class UserPatch(Partial(UserBase)):
    pass


class UserParams(Nullified(UserBase)):
    pass
