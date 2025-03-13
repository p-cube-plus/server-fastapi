from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.membership import MembershipRepository


@dataclass
class MembershipContext(CRUDContext):
    repo: MembershipRepository = None
