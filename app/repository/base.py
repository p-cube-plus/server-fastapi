from typing import Generic, Sequence, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.entity.base import BaseEntity

Entity = TypeVar("Entity", bound=BaseEntity)


class BaseRepository(Generic[Entity]):
    def __init__(self, db: AsyncSession):
        self.db = db
        self._entity_type: Type[Entity] = None

    async def find_all(self) -> Sequence[Entity]:
        stmt = select(self._entity_type)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def find_by_id(self, id: int) -> Entity | None:
        stmt = select(self._entity_type).where(self._entity_type.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, entity: Entity) -> Entity:
        self.db.add(entity)
        await self.db.flush()
        await self.db.refresh(entity)
        return entity

    async def update(self, entity: Entity) -> Entity:
        await self.db.merge(entity)
        await self.db.flush()
        return entity

    async def delete(self, entity: Entity) -> None:
        await self.db.delete(entity)
        await self.db.flush()
