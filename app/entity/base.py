from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class EntityMeta(type(DeclarativeBase)):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], BaseModel):
            instance = cls(**args[0].model_dump(exclude_unset=True))
            return instance
        return super().__call__(*args, **kwargs)


class BaseEntity(DeclarativeBase, metaclass=EntityMeta):
    @classmethod
    def columns(cls):
        return cls.__table__.columns
