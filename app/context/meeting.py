from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.meeting import MeetingRepository


@dataclass
class MeetingContext(CRUDContext):
    repo: MeetingRepository = None
