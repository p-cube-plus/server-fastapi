from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.user_attendance import UserAttendanceContext
from app.dto.user_attendance import UserAttendanceDTO
from app.service.base import CRUDService


@dataclass
class UserAttendanceService(CRUDService[UserAttendanceDTO]):
    crud: Annotated[UserAttendanceContext, Depends()]
