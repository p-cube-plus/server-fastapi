from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import DatabaseSession
from app.database.mysql import MySQLDatabase
from app.dto.user import UserCreate, UserDelete, UserRead, UserUpdate
from app.entity.user import UserEntity

from .base import CRUDRepository


class UserRepository(
    CRUDRepository[UserEntity, UserCreate, UserRead, UserUpdate, UserDelete]
):
    def __init__(self, db: Annotated[DatabaseSession, Depends(MySQLDatabase)]):
        self.db = db

    async def get_by_name(self, name: str) -> UserRead | None:
        stmt = select(UserEntity).where(UserEntity.name == name)
        return await self.db.execute(stmt)
