from dataclasses import dataclass

from app.dto.profile import ProfileDTO
from app.entity.profile import ProfileEntity

from .base import CRUDRepository


@dataclass
class ProfileRepository(
    CRUDRepository[
        ProfileEntity,
        ProfileDTO,
    ]
):
    pass
