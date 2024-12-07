from typing import Generic, Sequence, TypeVar, get_args

from sqlalchemy import select

from app.database.base import DatabaseSession
from app.entity.base import BaseEntity

Entity = TypeVar("Entity", bound=BaseEntity)


class CRUDRepository(Generic[Entity]):
    @classmethod
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        for base in cls.__orig_bases__:
            if hasattr(base, "__origin__") and base.__origin__ is CRUDRepository:
                instance.__entity_type = get_args(base)[0]
                break

        for arg in (*args, *kwargs.values()):
            if issubclass(type(arg), DatabaseSession):
                instance.__session = arg
                break
        else:
            raise ValueError("DatabaseSession instance must be provided")

        return instance

    async def find_all(self) -> Sequence[Entity]:
        stmt = select(self.__entity_type)
        result = await self.__session.execute(stmt)
        return result.scalars().all()

    async def find_by_id(self, id: int) -> Entity | None:
        stmt = select(self.__entity_type).where(self.__entity_type.id == id)
        result = await self.__session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, entity: Entity) -> Entity:
        self.__session.add(entity)
        return entity

    async def update(self, entity: Entity) -> Entity:
        await self.__session.merge(entity)
        return entity

    async def delete(self, entity: Entity) -> None:
        await self.__session.delete(entity)
