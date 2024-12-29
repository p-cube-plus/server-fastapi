from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance import AttendanceContext
from app.dto.attendance import AttendanceDTO
from app.service.base import CRUDService


@dataclass
class AttendanceService(CRUDService[AttendanceDTO]):
    crud: Annotated[AttendanceContext, Depends()]
