from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.academic import AcademicContext
from app.dto.academic import AcademicDTO
from app.service.base import CRUDService


@dataclass
class AcademicService(CRUDService[AcademicDTO]):
    crud: Annotated[AcademicContext, Depends()]
