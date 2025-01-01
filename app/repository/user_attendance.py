from dataclasses import dataclass

from app.dto.user_attendance import UserAttendanceDTO
from app.entity.user_attendance import UserAttendanceEntity

from .base import CRUDRepository


@dataclass
class UserAttendanceRepository(
    CRUDRepository[
        UserAttendanceEntity,
        UserAttendanceDTO,
    ]
):
    pass
