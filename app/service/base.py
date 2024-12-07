from typing import Generic, TypeVar

from app.entity.base import BaseEntity
from app.repository.base import CRUDRepository

Entity = TypeVar("Entity", bound=BaseEntity)
Repository = TypeVar("Repository", bound=CRUDRepository[Entity])


class BaseService(Generic[Entity, Repository]):
    pass
