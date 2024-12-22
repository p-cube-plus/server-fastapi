from dataclasses import dataclass

from app.dto.attendance import (
    AttendanceCreate,
    AttendanceID,
    AttendanceRead,
    AttendanceUpdate,
)
from app.entity.attendance import AttendanceEntity

from .base import CRUDRepository


@dataclass
class AttendanceRepository(
    CRUDRepository[
        AttendanceEntity,
        int,
        AttendanceCreate,
        AttendanceRead,
        AttendanceUpdate,
    ]
):
    pass
