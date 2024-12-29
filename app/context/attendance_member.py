from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.attendance_member import AttendanceMemberRepository


@dataclass
class AttendanceMemberContext(CRUDContext):
    repo: AttendanceMemberRepository = None
