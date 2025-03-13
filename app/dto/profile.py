from dataclasses import Field
from datetime import date

from .base import BaseDTO, Nullified, Partial, QueryParamsDTO


class ProfileID(BaseDTO):
    id: int


class ProfileBase(BaseDTO):
    user_id: int
    phone_number: str | None = None
    profile_image: str | None = None
    birth_date: date | None = None
    description: str | None = None


class ProfileDTO(ProfileBase, ProfileID):
    pass


class ProfileParam(Partial(ProfileBase)):
    pass


class ProfilePost(ProfileBase):
    pass


class ProfilePut(ProfileBase):
    pass


class ProfilePatch(Partial(ProfileBase)):
    pass


class ProfileParams(Nullified(ProfileBase), QueryParamsDTO):
    pass
