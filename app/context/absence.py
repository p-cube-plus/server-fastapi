from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.absence import AbsenceRepository


@dataclass
class AbsenceContext(CRUDContext):
    repo: AbsenceRepository = None
