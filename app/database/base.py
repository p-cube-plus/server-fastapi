from __future__ import annotations

from inspect import Parameter, Signature
from typing import Any, AsyncGenerator, ClassVar, Dict, Protocol, Type, TypeVar

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class DatabaseSessionMeta(type(AsyncSession)):
    __signature__ = Signature([])

    async def __call__(
        cls, *args, database_class: Type[BaseDatabase] = None, **kwargs
    ) -> AsyncGenerator[DatabaseSession, None]:
        if "bind" in kwargs:
            yield super().__call__(*args, **kwargs)
            return
        if database_class is None:
            from app.database.mysql import MySQLDatabase

            database_class = MySQLDatabase
        async for session in database_class():
            yield session


class DatabaseSession(AsyncSession, metaclass=DatabaseSessionMeta):

    def __init__(self, *args, database_class: Type[BaseDatabase] = None, **kwargs):
        super().__init__(*args, **kwargs)


class DatabaseURL(Protocol):
    DRIVER: ClassVar[str]

    def __new__(cls, settings: Dict[str, Any]) -> URL: ...


class DatabaseConnection:
    def __init__(self, url_type: Type[DatabaseURL], settings: Dict[str, Any]):
        self.engine = create_async_engine(url_type(settings))
        self.session_maker = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=DatabaseSession
        )


class DatabaseMeta(type):
    async def __call__(cls: BaseDatabase) -> AsyncGenerator[DatabaseSession, None]:
        session = await anext(cls._connection.session_maker())
        try:
            yield session
        finally:
            await session.close()


class BaseDatabase(metaclass=DatabaseMeta):
    _connection: DatabaseConnection

    @classmethod
    async def shutdown(cls) -> None:
        await cls._connection.engine.dispose()
