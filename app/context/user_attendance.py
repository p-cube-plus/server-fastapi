from dataclasses import dataclass

from app.context.base import BaseContext, CRUDContext
from app.repository.attendance import AttendanceRepository
from app.repository.user_attendance import UserAttendanceRepository


@dataclass
class UserAttendanceContext(CRUDContext):
    repo: UserAttendanceRepository = None


@dataclass
class UserAttendanceRequestContext(BaseContext):
    user_attendance_repo: UserAttendanceRepository = None
    attendance_repo: AttendanceRepository = None
