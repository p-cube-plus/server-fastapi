from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.meeting import MeetingContext
from app.dto.meeting import MeetingPayload, MeetingRequest, MeetingResponse
from app.service.base import CRUDService


@dataclass
class MeetingService(CRUDService[int, MeetingRequest, MeetingResponse, MeetingPayload]):
    crud: Annotated[MeetingContext, Depends()]
