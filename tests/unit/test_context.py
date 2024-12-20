import pytest

from app.context.user import UserContext
from app.database.mysql import MySQLDatabase
from app.repository.user import UserRepository


@pytest.mark.asyncio(scope="session")
async def test_auto_repository_initialization():
    async for session in MySQLDatabase():
        context = UserContext(session)

        assert isinstance(context.repo, UserRepository)
        assert context.repo.session == session
