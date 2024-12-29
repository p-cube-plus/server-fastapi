from fastapi import APIRouter

from . import attendance, user

router = APIRouter()
router.include_router(user.router, tags=["user"])
router.include_router(attendance.router, tags=["user > attendance"])
