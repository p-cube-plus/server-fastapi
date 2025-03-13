from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from app.context.membership import MembershipContext
from app.dto.membership import MembershipDTO
from app.service.base import CRUDService


@dataclass
class MembershipService(CRUDService[MembershipDTO]):
    crud: Annotated[MembershipContext, Depends()]
