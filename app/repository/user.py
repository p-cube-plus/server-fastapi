from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import DatabaseSession
from app.database.mysql import MySQLDatabase
from app.dto.user import UserCreate, UserID, UserRead, UserUpdate
from app.entity.user import UserEntity

from .base import CRUDRepository


@dataclass
class UserRepository(CRUDRepository[UserEntity, str, UserCreate, UserRead, UserUpdate]):
    async def get_by_name(self, name: str) -> UserRead | None:
        stmt = select(UserEntity).where(UserEntity.name == name)
        return await self.session.execute(stmt)
