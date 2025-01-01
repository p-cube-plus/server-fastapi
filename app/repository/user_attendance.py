from dataclasses import dataclass

from sqlalchemy import select

from app.dto.attendance import AttendanceDTO
from app.dto.user import UserDTO
from app.dto.user_attendance import UserAttendanceDTO
from app.entity.attendance import AttendanceEntity
from app.entity.user import UserEntity
from app.entity.user_attendance import UserAttendanceEntity

from .base import CRUDRepository


@dataclass
class UserAttendanceRepository(
    CRUDRepository[
        UserAttendanceEntity,
        UserAttendanceDTO,
    ]
):

    async def get_user_attendance_records(
        self, *, user_id, **filters
    ) -> list[tuple[UserAttendanceDTO, AttendanceDTO]]:
        stmt = (
            select(UserAttendanceEntity, AttendanceEntity)
            .select_from(UserAttendanceEntity)
            .filter_by(user_id=user_id)
            .join(
                AttendanceEntity,
                UserAttendanceEntity.attendance_id == AttendanceEntity.id,
            )
            .filter_by(**filters)
        )
        return await self.session.execute(stmt)

    async def get_attendance_user_records(
        self, *, attendance_id, **filters
    ) -> list[tuple[UserAttendanceDTO, UserDTO]]:
        stmt = (
            select(UserAttendanceEntity, UserEntity)
            .select_from(UserAttendanceEntity)
            .filter_by(attendance_id=attendance_id)
            .join(UserEntity, UserAttendanceEntity.user_id == UserEntity.id)
            .filter_by(**filters)
        )
        return await self.session.execute(stmt)
