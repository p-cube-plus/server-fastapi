from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, create_model
from pydantic_core import PydanticUndefined
from sqlalchemy.orm import DeclarativeBase


class DTOMeta(type(BaseModel)):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], DeclarativeBase):
            instance = cls.model_validate(args[0])
            return instance
        return super().__call__(*args, **kwargs)


class BaseDTO(BaseModel, metaclass=DTOMeta):
    model_config = ConfigDict(from_attributes=True, frozen=False)

    def dict(self, *args, exclude_unset=True, **kwargs):
        return self.model_dump(*args, exclude_unset=exclude_unset, **kwargs)


DTO = TypeVar("DTO", bound=BaseDTO)

_partial_cache: dict[type, type] = {}


def Partial(cls: type[DTO]) -> type[DTO]:
    if cls in _partial_cache:
        return _partial_cache[cls]

    fields = {
        field_name: (Optional[field_type.annotation], None)
        for field_name, field_type in cls.model_fields.items()
        if field_type.is_required()
    }

    partial_cls = create_model(f"Partial{cls.__name__}", __base__=cls, **fields)
    _partial_cache[cls] = partial_cls

    return partial_cls


_nullable_cache: dict[type, type] = {}


def Nullified(cls: type[DTO]) -> type[DTO]:
    if cls in _nullable_cache:
        return _nullable_cache[cls]

    fields = {
        field_name: (Optional[field_type.annotation], None)
        for field_name, field_type in cls.model_fields.items()
    }

    nullable_cls = create_model(f"Nullable{cls.__name__}", __base__=cls, **fields)
    _nullable_cache[cls] = nullable_cls

    return nullable_cls
