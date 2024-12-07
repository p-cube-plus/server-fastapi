from typing import Generic, Sequence, Type, TypeVar

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.entity.base import BaseEntity
from app.repository.base import CRUDRepository

Entity = TypeVar("Entity", bound=BaseEntity)
Repository = TypeVar("Repository", bound=CRUDRepository[Entity])


class BaseService(Generic[Entity, Repository]):
    def __init__(self, repository: Repository):
        self.repository = repository
