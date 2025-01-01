from dataclasses import dataclass
from datetime import datetime, time
from typing import Annotated

from fastapi import Depends

from app.context.user_attendance import (
    UserAttendanceContext,
    UserAttendanceRequestContext,
)
from app.dto.attendance import AttendanceDTO
from app.dto.user import UserDTO
from app.dto.user_attendance import UserAttendanceDTO
from app.service.base import CRUDService


@dataclass
class UserAttendanceService(CRUDService[UserAttendanceDTO]):
    crud: Annotated[UserAttendanceContext, Depends()]
    request_context: Annotated[UserAttendanceRequestContext, Depends()]

    async def get_user_attendance_list(
        self, *, user_id: int, **filters
    ) -> list[tuple[UserAttendanceDTO, AttendanceDTO]]:
        async with self.crud as crud:
            return await crud.repo.get_user_attendance_list(user_id=user_id, **filters)

    async def get_attendance_user_list(
        self, *, attendance_id: int, **filters
    ) -> list[tuple[UserAttendanceDTO, UserDTO]]:
        async with self.crud as crud:
            return await crud.repo.get_attendance_user_list(
                attendance_id=attendance_id, **filters
            )

    async def request_user_attendance(
        self, *, user_id: int, attendance_id: int, current_datetime: datetime
    ) -> UserAttendanceDTO:
        async with self.request_context as context:
            attendance = (await context.attendance_repo.get(id=attendance_id))[0]
            user_attendance = await context.user_attendance_repo.get(
                user_id=user_id, attendance_id=attendance_id
            )
            if not user_attendance:
                user_attendance = await context.user_attendance_repo.create(
                    [UserAttendanceDTO(user_id=user_id, attendance_id=attendance_id)]
                )
            user_attendance = user_attendance[0]

            current_date = current_datetime.date()
            current_time = current_datetime.time()

            if (
                current_date <= attendance.date
                and current_time < attendance.second_auth_start_time
            ):
                user_attendance.first_auth_time = current_time
            else:
                user_attendance.second_auth_time = current_time
            user_attendance = await context.user_attendance_repo.update(user_attendance)
            return user_attendance[0]
