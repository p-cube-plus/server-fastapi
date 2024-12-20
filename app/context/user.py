from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.user import UserRepository


@dataclass
class UserContext(CRUDContext):
    repo: UserRepository = None
