from dataclasses import dataclass

from app.dto.attendance import AttendanceDTO
from app.entity.attendance import AttendanceEntity

from .base import CRUDRepository


@dataclass
class AttendanceRepository(
    CRUDRepository[
        AttendanceEntity,
        AttendanceDTO,
    ]
):
    pass
