from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, HTTPException

from app.context.user import UserContext
from app.dto.user import UserCreate, UserDelete, UserRead, UserUpdate
from app.repository.user import UserRepository
from app.service.base import BaseService, CRUDService


@dataclass
class UserService(CRUDService):
    crud: Annotated[UserContext, Depends()]

    async def get_by_name(self, name: str) -> UserRead:
        async with self.crud as crud:
            return await crud.repo.get_by_name(name)
