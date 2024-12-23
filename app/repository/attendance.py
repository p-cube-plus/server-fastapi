from dataclasses import dataclass

from app.dto.attendance import (
    AttendanceID,
    AttendancePayload,
    AttendanceRequest,
    AttendanceResponse,
)
from app.entity.attendance import AttendanceEntity

from .base import CRUDRepository


@dataclass
class AttendanceRepository(
    CRUDRepository[
        AttendanceEntity,
        AttendanceRequest,
        AttendanceResponse,
        AttendancePayload,
    ]
):
    pass
