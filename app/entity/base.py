from typing import Type

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class EntityRegistry:
    _registry: dict[str, Type["BaseEntity"]] = {}

    @classmethod
    def register(cls, entity_cls: Type["BaseEntity"]):
        cls._registry[entity_cls.__tablename__] = entity_cls

    @classmethod
    def __getitem__(cls, table_name: str) -> Type["BaseEntity"]:
        return cls._registry[table_name]


class EntityMeta(type(DeclarativeBase)):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)

        if "__tablename__" in attrs:
            EntityRegistry.register(cls)

        return cls

    def __call__(cls, *args, **kwargs):
        if len(args) == 1:
            if isinstance(args[0], BaseModel):
                instance = cls(**args[0].model_dump(exclude_unset=True))
                return instance
            elif args[0] is None:
                return None
        return super().__call__(*args, **kwargs)


class BaseEntity(DeclarativeBase, metaclass=EntityMeta):
    @classmethod
    def columns(cls):
        return cls.__table__.columns
