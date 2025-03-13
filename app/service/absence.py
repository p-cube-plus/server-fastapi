from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.absence import AbsenceContext
from app.dto.absence import AbsenceDTO
from app.service.base import CRUDService


@dataclass
class AbsenceService(CRUDService[AbsenceDTO]):
    crud: Annotated[AbsenceContext, Depends()]
