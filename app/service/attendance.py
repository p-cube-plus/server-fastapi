from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance import AttendanceContext
from app.dto.attendance import AttendanceCreate, AttendanceRead, AttendanceUpdate
from app.service.base import CRUDService


@dataclass
class AttendanceService(
    CRUDService[int, AttendanceCreate, AttendanceRead, AttendanceUpdate]
):
    crud: Annotated[AttendanceContext, Depends()]
