from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance import AttendanceContext
from app.dto.attendance import AttendancePayload, AttendanceRequest, AttendanceResponse
from app.service.base import CRUDService


@dataclass
class AttendanceService(
    CRUDService[AttendanceRequest, AttendanceResponse, AttendancePayload]
):
    crud: Annotated[AttendanceContext, Depends()]
