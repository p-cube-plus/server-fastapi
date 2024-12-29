from dataclasses import dataclass

from sqlalchemy import select

from app.dto.user import UserDTO
from app.entity.user import UserEntity

from .base import CRUDRepository


@dataclass
class UserRepository(CRUDRepository[UserEntity, UserDTO]):
    async def get_by_name(self, name: str) -> UserDTO | None:
        stmt = select(UserEntity).where(UserEntity.name == name)
        return await self.session.execute(stmt)
