from datetime import date
from typing import Optional

from .base import BaseDTO


class UserResponseDTO(BaseDTO):
    id: str
    is_signed: bool = False
    name: str
    level: int
    grade: int
    part_index: int
    profile_image: Optional[str] = None
    univ: Optional[str] = None
    last_cleaning: Optional[date] = None
    rest_type: int
    etc_message: Optional[str] = None
    absent_reason: Optional[str] = None
    absent_detail_reason: Optional[str] = None
    phone_number: Optional[str] = None
    join_date: Optional[date] = None
    birth_date: Optional[date] = None
    birth_month: Optional[int] = None
    birth_day: Optional[int] = None
    major: Optional[str] = None
    student_id: Optional[str] = None
    is_next_birth: bool = False
    return_plan_date: Optional[date] = None
    workshop_count: Optional[int] = None
    gogoma: Optional[str] = None
    warning_point: int = 0
    fcm_token: Optional[str] = None
    api_access_level: int = 0
