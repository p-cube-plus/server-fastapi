from dataclasses import dataclass

from app.dto.membership import MembershipDTO
from app.entity.membership import MembershipEntity

from .base import CRUDRepository


@dataclass
class MembershipRepository(
    CRUDRepository[
        MembershipEntity,
        MembershipDTO,
    ]
):
    pass
