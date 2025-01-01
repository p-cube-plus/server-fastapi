from app.core.routing import CustomAPIRouter

from . import attendance, user

router = CustomAPIRouter()
router.include_router(attendance.router, tags=["attendance"])
router.include_router(user.router, tags=["attendance > user"])
