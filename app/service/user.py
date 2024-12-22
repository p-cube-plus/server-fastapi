from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.user import UserContext
from app.dto.user import UserCreate, UserRead, UserUpdate
from app.service.base import CRUDService


@dataclass
class UserService(CRUDService[str, UserCreate, UserRead, UserUpdate]):
    crud: Annotated[UserContext, Depends()]

    async def get_by_name(self, name: str) -> UserRead:
        async with self.crud as crud:
            return await crud.repo.get_by_name(name)
