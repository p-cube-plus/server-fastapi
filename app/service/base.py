from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar, Union

from fastapi import Depends

from app.context.base import CRUDContext
from app.dto.base import BaseDTO
from app.entity.base import BaseEntity

ID = TypeVar("ID", bound=Union[int, str])
RequestDTO = TypeVar("RequestDTO", bound=BaseDTO)
ResponseDTO = TypeVar("ResponseDTO", bound=BaseDTO)
PayloadDTO = TypeVar("PayloadDTO", bound=BaseDTO)


@dataclass
class BaseService:
    pass


@dataclass
class CRUDService(BaseService, Generic[ID, RequestDTO, ResponseDTO, PayloadDTO]):
    crud: Annotated[CRUDContext, Depends()]

    async def get_all(self, payload_dto: PayloadDTO) -> list[ResponseDTO]:
        async with self.crud as crud:
            return await crud.repo.get_all(payload_dto)

    async def get(self, id: ID) -> ResponseDTO | None:
        async with self.crud as crud:
            return await crud.repo.get(id)

    async def create(self, request_dto: RequestDTO) -> ResponseDTO:
        async with self.crud as crud:
            result = await crud.repo.create(request_dto)
            await crud.commit()
            return result

    async def update(self, id: ID, payload_dto: PayloadDTO) -> ResponseDTO:
        async with self.crud as crud:
            result = await crud.repo.update(id, payload_dto)
            await crud.commit()
            return result

    async def delete(self, id: ID) -> ResponseDTO:
        async with self.crud as crud:
            result = await crud.repo.delete(id)
            await crud.commit()
            return result
