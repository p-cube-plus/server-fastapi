from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.attendance_member import AttendanceMemberContext
from app.dto.attendance_member import AttendanceMemberDTO
from app.service.base import CRUDService


@dataclass
class AttendanceMemberService(CRUDService[AttendanceMemberDTO]):
    crud: Annotated[AttendanceMemberContext, Depends()]
