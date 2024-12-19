from dataclasses import dataclass

from app.context.base import BaseContext
from app.repository.user import UserRepository


@dataclass
class UserContext(BaseContext):
    users: UserRepository = None
