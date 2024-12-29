from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar

from fastapi import Depends

from app.context.base import CRUDContext
from app.dto.base import BaseDTO

DTO = TypeVar("DTO", bound=BaseDTO)


@dataclass
class BaseService:
    pass


@dataclass
class CRUDService(BaseService, Generic[DTO]):
    crud: Annotated[CRUDContext, Depends()]

    async def get(self, **filters) -> list[DTO]:
        async with self.crud as crud:
            return await crud.repo.get(**filters)

    async def create(self, dto_list: list[BaseDTO]) -> list[DTO]:
        async with self.crud as crud:
            result = await crud.repo.create(dto_list)
            await crud.commit()
            return result

    async def update(self, dto: BaseDTO, *, exclude_unset=True, **filters) -> list[DTO]:
        async with self.crud as crud:
            result = await crud.repo.update(dto, exclude_unset=exclude_unset, **filters)
            await crud.commit()
            return result

    async def delete(self, **filters) -> list[DTO]:
        async with self.crud as crud:
            result = await crud.repo.delete(**filters)
            await crud.commit()
            return result
