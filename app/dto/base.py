from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        from_attributes = True

    def __call__(self, Entity):
        return Entity(**self.model_dump())
