from fastapi import Depends, HTTPException

from app.dto.user import UserResponseDTO
from app.entity.user import UserEntity
from app.repository.user import UserRepository
from app.service.base import BaseService


class UserService(BaseService[UserEntity, UserRepository]):
    def __init__(self, repository: UserRepository = Depends()):
        super().__init__(repository)

    async def find_all(self) -> list[UserResponseDTO]:
        users = await self.repository.find_all()
        return [UserResponseDTO.model_validate(user) for user in users]

    async def find_by_id(self, user_id: int) -> UserResponseDTO:
        user = await self.repository.find_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponseDTO.model_validate(user)

    async def find_by_name(self, name: str) -> UserResponseDTO:
        user = await self.repository.find_by_name(name)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponseDTO.model_validate(user)
