from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.user_attendance import UserAttendanceRepository


@dataclass
class UserAttendanceContext(CRUDContext):
    repo: UserAttendanceRepository = None
