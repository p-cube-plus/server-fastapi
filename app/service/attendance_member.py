from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance_member import AttendanceMemberContext
from app.dto.attendance_member import (
    AttendanceMemberPayload,
    AttendanceMemberRequest,
    AttendanceMemberResponse,
)
from app.service.base import CRUDService


@dataclass
class AttendanceMemberService(
    CRUDService[
        AttendanceMemberRequest, AttendanceMemberResponse, AttendanceMemberPayload
    ]
):
    crud: Annotated[AttendanceMemberContext, Depends()]
