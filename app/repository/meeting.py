from dataclasses import dataclass

from app.dto.meeting import MeetingID, MeetingPayload, MeetingRequest, MeetingResponse
from app.entity.meeting import MeetingEntity

from .base import CRUDRepository


@dataclass
class MeetingRepository(
    CRUDRepository[
        MeetingEntity,
        int,
        MeetingRequest,
        MeetingResponse,
        MeetingPayload,
    ]
):
    pass
