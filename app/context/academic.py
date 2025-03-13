from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.academic import AcademicRepository


@dataclass
class AcademicContext(CRUDContext):
    repo: AcademicRepository = None
