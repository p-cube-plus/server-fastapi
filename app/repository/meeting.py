from dataclasses import dataclass

from app.dto.meeting import MeetingCreate, MeetingDelete, MeetingRead, MeetingUpdate
from app.entity.meeting import MeetingEntity

from .base import CRUDRepository


@dataclass
class MeetingRepository(
    CRUDRepository[
        MeetingEntity,
        MeetingCreate,
        MeetingRead,
        MeetingUpdate,
        MeetingDelete,
    ]
):
    pass
