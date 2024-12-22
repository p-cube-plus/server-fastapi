from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar, Union

from fastapi import Depends

from app.context.base import CRUDContext
from app.dto.base import BaseDTO
from app.entity.base import BaseEntity

ID = TypeVar("ID", bound=Union[int, str])
CreateDTO = TypeVar("CreateDTO", bound=BaseDTO)
ReadDTO = TypeVar("ReadDTO", bound=BaseDTO)
UpdateDTO = TypeVar("UpdateDTO", bound=BaseDTO)


@dataclass
class BaseService:
    pass


@dataclass
class CRUDService(BaseService, Generic[ID, CreateDTO, ReadDTO, UpdateDTO]):
    crud: Annotated[CRUDContext, Depends()]

    async def get_all(self) -> list[ReadDTO]:
        async with self.crud as crud:
            return await crud.repo.get_all()

    async def get(self, id: ID) -> ReadDTO | None:
        async with self.crud as crud:
            return await crud.repo.get(id)

    async def create(self, create_dto: CreateDTO) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.create(create_dto)
            await crud.commit()
            return result

    async def update(self, id: ID, update_dto: UpdateDTO) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.update(id, update_dto)
            await crud.commit()
            return result

    async def delete(self, id: ID) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.delete(id)
            await crud.commit()
            return result
