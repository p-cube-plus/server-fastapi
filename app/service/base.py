from dataclasses import dataclass
from inspect import Parameter, signature
from typing import (
    Annotated,
    Generic,
    Type,
    TypeAliasType,
    TypeVar,
    get_args,
    get_type_hints,
)

from fastapi import Depends
from sqlalchemy import cast

from app.context.base import CRUDContext
from app.context.user import UserContext
from app.dto.base import BaseDTO
from app.entity.base import BaseEntity
from app.repository.base import CRUDRepository

CreateDTO = TypeVar("CreateDTO", bound=BaseDTO)
ReadDTO = TypeVar("ReadDTO", bound=BaseDTO)
UpdateDTO = TypeVar("UpdateDTO", bound=BaseDTO)
DeleteDTO = TypeVar("DeleteDTO", bound=BaseDTO)


@dataclass
class BaseService:
    pass


@dataclass
class CRUDService(BaseService):
    crud: Annotated[CRUDContext, Depends()]

    async def get_all(self) -> list[ReadDTO]:
        async with self.crud as crud:
            return await crud.repo.get_all()

    async def get_by_id(self, id: int) -> ReadDTO | None:
        async with self.crud as crud:
            return await crud.repo.get_by_id(id)

    async def create(self, create_dto: CreateDTO) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.create(create_dto)
            await crud.commit()
            return result

    async def update(self, update_dto: UpdateDTO) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.update(update_dto)
            await crud.commit()
            return result

    async def delete(self, delete_dto: DeleteDTO) -> ReadDTO:
        async with self.crud as crud:
            result = await crud.repo.delete(delete_dto)
            await crud.commit()
            return result
