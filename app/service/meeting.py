from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.meeting import MeetingContext
from app.dto.meeting import MeetingCreate, MeetingRead, MeetingUpdate
from app.service.base import CRUDService


@dataclass
class MeetingService(CRUDService[int, MeetingCreate, MeetingRead, MeetingUpdate]):
    crud: Annotated[MeetingContext, Depends()]
