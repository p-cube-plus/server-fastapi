from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar, Union

from fastapi import Depends

from app.context.base import CRUDContext
from app.dto.base import BaseDTO
from app.entity.base import BaseEntity

RequestDTO = TypeVar("RequestDTO", bound=BaseDTO)
ResponseDTO = TypeVar("ResponseDTO", bound=BaseDTO)
PayloadDTO = TypeVar("PayloadDTO", bound=BaseDTO)


@dataclass
class BaseService:
    pass


@dataclass
class CRUDService(BaseService, Generic[RequestDTO, ResponseDTO, PayloadDTO]):
    crud: Annotated[CRUDContext, Depends()]

    async def get(self, **kwargs) -> list[ResponseDTO]:
        async with self.crud as crud:
            return await crud.repo.get(**kwargs)

    async def create(self, request_dto_list: list[RequestDTO]) -> list[ResponseDTO]:
        async with self.crud as crud:
            result = await crud.repo.create(request_dto_list)
            await crud.commit()
            return result

    async def replace(self, request_dto: RequestDTO, **kwargs) -> list[ResponseDTO]:
        async with self.crud as crud:
            result = await crud.repo.replace(request_dto, **kwargs)
            await crud.commit()
            return result

    async def update(self, payload_dto: PayloadDTO, **kwargs) -> list[ResponseDTO]:
        async with self.crud as crud:
            result = await crud.repo.update(payload_dto, **kwargs)
            await crud.commit()
            return result

    async def delete(self, **kwargs) -> list[ResponseDTO]:
        async with self.crud as crud:
            result = await crud.repo.delete(**kwargs)
            await crud.commit()
            return result
