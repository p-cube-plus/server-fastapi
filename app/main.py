from starlette.middleware.cors import CORSMiddleware

from app.api import attendance, meeting, user, user_attendance
from app.core.fastapi import CustomFastAPI

app = CustomFastAPI(docs_url="/", redoc_url=None)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, tags=["user"])
app.include_router(attendance.router, tags=["attendance"])
app.include_router(meeting.router, tags=["meeting"])
app.include_router(user_attendance.router, tags=["user_attendance"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
