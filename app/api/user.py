from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.user import UserRead
from app.service.user import UserService

router = APIRouter(
    prefix="/user",
)


@router.get("", response_model=list[UserRead])
async def get_user_list(service: UserService = Depends()):
    user_list = await service.get_all()
    return user_list
