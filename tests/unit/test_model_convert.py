import asyncio

import pytest
from sqlalchemy import inspect, select

from app.database.mysql import MySQLDatabase
from app.entity.user import UserEntity
from app.entity.user_attendance import UserAttendanceEntity
from app.repository.user import UserRepository
from app.repository.user_attendance import UserAttendanceRepository


@pytest.mark.asyncio(scope="session")
async def test_convert_dto_to_entity():
    async for db in MySQLDatabase():
        user_repo = UserRepository(db)
        user_dto = (await user_repo.get())[0]

    user_entity = UserEntity(user_dto)

    entity_dict = {
        c.key: getattr(user_entity, c.key)
        for c in inspect(user_entity).mapper.column_attrs
    }

    dto_dict = user_dto.dict()

    common_keys = set(entity_dict.keys()) & set(dto_dict.keys())
    for key in common_keys:
        assert entity_dict[key] == dto_dict[key]
