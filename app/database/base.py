from __future__ import annotations

from typing import Any, AsyncGenerator, ClassVar, Dict, Protocol, Type

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class DatabaseSession(AsyncSession):
    pass


class DatabaseURL(Protocol):
    DRIVER: ClassVar[str]

    def __new__(cls, settings: Dict[str, Any]) -> URL: ...


class DatabaseConnection:
    def __init__(self, url_type: Type[DatabaseURL], settings: Dict[str, Any]):
        self.engine = create_async_engine(url_type(settings))
        self.session_maker = async_sessionmaker(self.engine, expire_on_commit=False)


class DatabaseMeta(type):
    async def __call__(cls: BaseDatabase) -> AsyncGenerator[AsyncSession, None]:
        session = cls._connection.session_maker()
        try:
            yield session
        finally:
            await session.close()


class BaseDatabase(metaclass=DatabaseMeta):
    _connection: DatabaseConnection

    @classmethod
    async def shutdown(cls) -> None:
        await cls._connection.engine.dispose()
