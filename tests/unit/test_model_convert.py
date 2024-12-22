import asyncio

import pytest
from sqlalchemy import inspect

from app.database.mysql import MySQLDatabase
from app.dto.user import UserResponse
from app.entity.user import UserEntity
from app.repository.user import UserRepository


@pytest.mark.asyncio(scope="session")
async def test_convert_dto_to_entity():
    async for db in MySQLDatabase():
        user_repo = UserRepository(db)
        user_dto = (await user_repo.get_all())[0]

    user_entity = UserEntity(user_dto)

    entity_dict = {
        c.key: getattr(user_entity, c.key)
        for c in inspect(user_entity).mapper.column_attrs
    }

    dto_dict = user_dto.dict()

    common_keys = set(entity_dict.keys()) & set(dto_dict.keys())
    for key in common_keys:
        assert entity_dict[key] == dto_dict[key]
