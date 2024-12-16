from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import DeclarativeBase


class DTOMeta(type(BaseModel)):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], DeclarativeBase):
            instance = cls.model_validate(args[0])
            return instance
        return super().__call__(*args, **kwargs)


class BaseDTO(BaseModel, metaclass=DTOMeta):
    model_config = ConfigDict(from_attributes=True, frozen=False, extra="allow")

    def dict(self, *args, **kwargs):
        return self.model_dump(*args, exclude_unset=True, **kwargs)
