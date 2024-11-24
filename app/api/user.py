from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.user import UserResponseDTO
from app.service.user import UserService

router = APIRouter(
    prefix="/user",
)


@router.get("", response_model=list[UserResponseDTO])
async def get_user_list(service: UserService = Depends()):
    user_list = await service.find_all()
    return user_list
