from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import get_settings

settings = get_settings()["database"]

DB_URL = f"mysql+aiomysql://{settings['user']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['db']}"

engine = create_async_engine(DB_URL)

Session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        await db.close()
