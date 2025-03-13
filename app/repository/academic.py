from dataclasses import dataclass

from app.dto.academic import AcademicDTO
from app.entity.academic import AcademicEntity

from .base import CRUDRepository


@dataclass
class AcademicRepository(
    CRUDRepository[
        AcademicEntity,
        AcademicDTO,
    ]
):
    pass
