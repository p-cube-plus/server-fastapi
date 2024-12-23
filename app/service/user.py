from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.user import UserContext
from app.dto.user import UserPayload, UserRequest, UserResponse
from app.service.base import CRUDService


@dataclass
class UserService(CRUDService[UserRequest, UserResponse, UserPayload]):
    crud: Annotated[UserContext, Depends()]

    async def get_by_name(self, name: str) -> UserResponse:
        async with self.crud as crud:
            return await crud.repo.get_by_name(name)
