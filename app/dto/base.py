from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, create_model
from sqlalchemy.orm import DeclarativeBase


class DTOMeta(type(BaseModel)):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], DeclarativeBase):
            instance = cls.model_validate(args[0])
            return instance
        return super().__call__(*args, **kwargs)


class BaseDTO(BaseModel, metaclass=DTOMeta):
    model_config = ConfigDict(from_attributes=True, frozen=False)

    def dict(self, *args, **kwargs):
        return self.model_dump(*args, exclude_unset=True, **kwargs)


DTO = TypeVar("DTO", bound=BaseDTO)


def Partial(cls: type[DTO]) -> type[DTO]:
    fields = {
        field_name: (Optional[field_type.annotation], None)
        for field_name, field_type in cls.model_fields.items()
    }

    return create_model(f"Partial{cls.__name__}", **fields)
