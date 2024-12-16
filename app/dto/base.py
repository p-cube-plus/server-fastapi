from pydantic import BaseModel, ConfigDict

from app.entity.base import BaseEntity


class DTOMeta(type(BaseModel)):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], BaseEntity):
            instance = cls.model_validate(args[0])
            return instance
        return super().__call__(*args, **kwargs)


class BaseDTO(BaseModel, metaclass=DTOMeta):
    model_config = ConfigDict(from_attributes=True, frozen=False, extra="allow")
