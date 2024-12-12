from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        from_attributes = True
        frozen = False
        extra = "allow"
