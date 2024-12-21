import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import DatabaseSession
from app.database.mysql import MySQLDatabase
from app.database.sqlite import SQLiteDatabase


@pytest.mark.asyncio(scope="session")
async def test_database_session():
    async for session in MySQLDatabase():
        assert isinstance(session, DatabaseSession)
        assert type(session) == DatabaseSession

    async for session in DatabaseSession():
        assert isinstance(session, DatabaseSession)
        assert type(session) == DatabaseSession

    async for session in DatabaseSession(SQLiteDatabase):
        assert isinstance(session, DatabaseSession)
        assert type(session) == DatabaseSession
