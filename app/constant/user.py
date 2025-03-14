from enum import Enum


class UserRole(int, Enum):
    NONE = 0
    GUEST = 1
    USER = 2
    ADMIN = 3
    DEVELOPER = 4
