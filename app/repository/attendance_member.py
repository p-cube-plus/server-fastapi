from dataclasses import dataclass

from app.dto.attendance_member import AttendanceMemberDTO
from app.entity.attendance_member import AttendanceMemberEntity

from .base import CRUDRepository


@dataclass
class AttendanceMemberRepository(
    CRUDRepository[
        AttendanceMemberEntity,
        AttendanceMemberDTO,
    ]
):
    pass
