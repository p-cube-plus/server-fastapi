from typing import Annotated

from fastapi import Depends, HTTPException

from app.dto.user import UserCreate, UserDelete, UserRead, UserUpdate
from app.repository.user import UserRepository
from app.service.base import CRUDService


class UserService(CRUDService[UserCreate, UserRead, UserUpdate, UserDelete]):
    def __init__(self, repo: Annotated[UserRepository, Depends()]):
        self.repo = repo

    async def get_by_name(self, name: str) -> UserRead:
        return await self.repo.get_by_name(name)
