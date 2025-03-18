from starlette.middleware.cors import CORSMiddleware

from app.api import (
    absence,
    academic,
    attendance,
    auth,
    meeting,
    membership,
    profile,
    user,
)
from app.core.fastapi import CustomFastAPI
from app.core.security import JWTMiddleware

app = CustomFastAPI(docs_url="/", redoc_url=None)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(JWTMiddleware)

app.include_router(user.router)
app.include_router(attendance.router)
app.include_router(meeting.router, tags=["meeting"])
app.include_router(auth.router, tags=["auth"])
app.include_router(absence.router, tags=["absence"])
app.include_router(academic.router, tags=["academic"])
app.include_router(membership.router, tags=["membership"])
app.include_router(profile.router, tags=["profile"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
