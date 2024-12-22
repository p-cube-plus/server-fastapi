from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance import AttendanceContext
from app.service.base import CRUDService


@dataclass
class AttendanceService(CRUDService):
    crud: Annotated[AttendanceContext, Depends()]
