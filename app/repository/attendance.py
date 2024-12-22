from dataclasses import dataclass

from app.dto.attendance import (
    AttendanceCreate,
    AttendanceDelete,
    AttendanceRead,
    AttendanceUpdate,
)
from app.entity.attendance import AttendanceEntity

from .base import CRUDRepository


@dataclass
class AttendanceRepository(
    CRUDRepository[
        AttendanceEntity,
        AttendanceCreate,
        AttendanceRead,
        AttendanceUpdate,
        AttendanceDelete,
    ]
):
    pass
