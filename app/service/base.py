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

from sqlalchemy import cast

from app.dto.base import BaseDTO
from app.entity.base import BaseEntity
from app.repository.base import CRUDRepository

CreateDTO = TypeVar("CreateDTO", bound=BaseDTO)
ReadDTO = TypeVar("ReadDTO", bound=BaseDTO)
UpdateDTO = TypeVar("UpdateDTO", bound=BaseDTO)
DeleteDTO = TypeVar("DeleteDTO", bound=BaseDTO)


class BaseService:
    pass


class CRUDService(BaseService, Generic[CreateDTO, ReadDTO, UpdateDTO, DeleteDTO]):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        for arg in (*args, *kwargs.values()):
            if issubclass(type(arg), CRUDRepository):
                instance.__repo = arg
                break
        else:
            raise ValueError("CRUDRepository instance must be provided")

        return instance

    @property
    def __repository(self) -> CRUDRepository:
        return self.__repo

    async def get_all(self) -> list[ReadDTO]:
        return await self.__repository.get_all()

    async def get_by_id(self, id: int) -> ReadDTO | None:
        return await self.__repository.get_by_id(id)

    async def create(self, create_dto: CreateDTO) -> ReadDTO:
        return await self.__repository.create(create_dto)

    async def update(self, update_dto: UpdateDTO) -> ReadDTO:
        return await self.__repository.create(update_dto)

    async def delete(self, delete_dto: DeleteDTO) -> ReadDTO:
        return await self.__repository.delete(delete_dto)
