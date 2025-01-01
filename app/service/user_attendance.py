from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.user_attendance import UserAttendanceContext
from app.dto.attendance import AttendanceDTO
from app.dto.user import UserDTO
from app.dto.user_attendance import UserAttendanceDTO
from app.service.base import CRUDService


@dataclass
class UserAttendanceService(CRUDService[UserAttendanceDTO]):
    crud: Annotated[UserAttendanceContext, Depends()]

    async def get_user_attendance_records(
        self, *, user_id, **filters
    ) -> list[tuple[UserAttendanceDTO, AttendanceDTO]]:
        async with self.crud as crud:
            return await crud.repo.get_user_attendance_records(
                user_id=user_id, **filters
            )

    async def get_attendance_user_records(
        self, *, attendance_id, **filters
    ) -> list[tuple[UserAttendanceDTO, UserDTO]]:
        async with self.crud as crud:
            return await crud.repo.get_attendance_user_records(
                attendance_id=attendance_id, **filters
            )
