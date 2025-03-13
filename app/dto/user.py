from dataclasses import Field
from datetime import date

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class UserID(BaseDTO):
    id: int


class UserBase(BaseDTO):
    hash: str
    is_signed: bool
    name: str
    fcm_token: str | None = None
    role: int = 0


class UserDTO(UserBase, UserID):
    pass


class UserParam(Partial(UserBase)):
    pass


class UserPost(UserBase):
    pass


class UserPut(UserBase):
    pass


class UserPatch(Partial(UserBase)):
    pass


class UserParams(Nullified(UserBase), QueryParamsDTO):
    pass
