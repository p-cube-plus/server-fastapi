from dataclasses import dataclass

from app.context.base import CRUDContext
from app.repository.profile import ProfileRepository


@dataclass
class ProfileContext(CRUDContext):
    repo: ProfileRepository = None
