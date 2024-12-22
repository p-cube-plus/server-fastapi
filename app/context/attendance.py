from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.attendance import AttendanceRepository


@dataclass
class AttendanceContext(CRUDContext):
    repo: AttendanceRepository = None
