from typing import Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.entity.user import UserEntity

from .base import BaseRepository


class UserRepository(BaseRepository[UserEntity]):
    def __init__(self, db: AsyncSession = Depends(get_db)):
        super().__init__(db)
        self._entity_type = UserEntity

    async def find_by_name(self, name: str) -> UserEntity | None:
        stmt = select(UserEntity).where(UserEntity.name == name)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
