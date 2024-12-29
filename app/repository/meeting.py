from dataclasses import dataclass

from app.dto.meeting import MeetingDTO
from app.entity.meeting import MeetingEntity

from .base import CRUDRepository


@dataclass
class MeetingRepository(
    CRUDRepository[
        MeetingEntity,
        MeetingDTO,
    ]
):
    pass
