from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.meeting import MeetingContext
from app.service.base import CRUDService


@dataclass
class MeetingService(CRUDService):
    crud: Annotated[MeetingContext, Depends()]
