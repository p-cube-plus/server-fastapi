from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.profile import ProfileContext
from app.dto.profile import ProfileDTO
from app.service.base import CRUDService


@dataclass
class ProfileService(CRUDService[ProfileDTO]):
    crud: Annotated[ProfileContext, Depends()]
