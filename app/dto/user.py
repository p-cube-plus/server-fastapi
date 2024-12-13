from datetime import date

from .base import BaseDTO


class UserBase(BaseDTO):
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


class UserRead(UserBase):
    id: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseDTO):
    id: str
    is_signed: bool | None = None
    name: str | None = None
    level: int | None = None
    grade: int | None = None
    part_index: int | None = None
    profile_image: str | None = None
    univ: str | None = None
    last_cleaning: date | None = None
    rest_type: int | None = None
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
    is_next_birth: bool | None = None
    return_plan_date: date | None = None
    workshop_count: int | None = None
    gogoma: str | None = None
    warning_point: int | None = None
    fcm_token: str | None = None
    api_access_level: int | None = None


class UserDelete(BaseDTO):
    id: str
