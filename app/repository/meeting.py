from dataclasses import dataclass

from app.dto.meeting import MeetingCreate, MeetingID, MeetingRead, MeetingUpdate
from app.entity.meeting import MeetingEntity

from .base import CRUDRepository


@dataclass
class MeetingRepository(
    CRUDRepository[
        MeetingEntity,
        int,
        MeetingCreate,
        MeetingRead,
        MeetingUpdate,
    ]
):
    pass
