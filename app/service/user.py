from typing import Annotated

from fastapi import Depends, HTTPException

from app.dto.user import UserRead
from app.repository.user import UserRepository


class UserService:
    def __init__(self, repo: Annotated[UserRepository, Depends()]):
        self.repo = repo

    async def find_all(self) -> list[UserRead]:
        users = await self.repo.find_all()
        return [UserRead.model_validate(user) for user in users]

    async def find_by_id(self, user_id: int) -> UserRead:
        user = await self.repo.find_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserRead.model_validate(user)

    async def find_by_name(self, name: str) -> UserRead:
        user = await self.repo.find_by_name(name)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserRead.model_validate(user)
