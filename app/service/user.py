from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.user import UserContext
from app.dto.user import UserDTO
from app.service.base import CRUDService


@dataclass
class UserService(CRUDService[UserDTO]):
    crud: Annotated[UserContext, Depends()]

    async def get_by_name(self, name: str) -> UserDTO:
        async with self.crud as crud:
            return await crud.repo.get_by_name(name)
