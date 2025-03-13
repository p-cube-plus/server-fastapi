from dataclasses import dataclass

from app.dto.absence import AbsenceDTO
from app.entity.absence import AbsenceEntity

from .base import CRUDRepository


@dataclass
class AbsenceRepository(
    CRUDRepository[
        AbsenceEntity,
        AbsenceDTO,
    ]
):
    pass
