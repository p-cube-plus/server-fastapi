from dataclasses import dataclass, field
from typing import Annotated

from fastapi import Depends

from app.database.base import DatabaseSession
from app.database.mysql import MySQLDatabase
from app.repository.base import BaseRepository


class ContextMeta(type):
    def __new__(mcs, name, bases, attrs):
        annotations = attrs.get("__annotations__", {})
        print(f"attrs = {attrs}")
        print(annotations)
        repo_fields = {
            field_name: field_type
            for field_name, field_type in annotations.items()
            if isinstance(field_type, type) and issubclass(field_type, BaseRepository)
        }

        for field_name, field_type in repo_fields.items():
            attrs[field_name] = attrs.get(field_name) or field(default=None)

        post_init = attrs.get("__post_init__")

        def __post_init__(self):
            if post_init:
                post_init(self)

            for field_name, field_type in repo_fields.items():
                if getattr(self, field_name) is None:
                    setattr(self, field_name, field_type(self.session))

        attrs["__post_init__"] = __post_init__

        return super().__new__(mcs, name, bases, attrs)


@dataclass
class BaseContext(metaclass=ContextMeta):
    session: Annotated[DatabaseSession, Depends(MySQLDatabase)]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rollback()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
