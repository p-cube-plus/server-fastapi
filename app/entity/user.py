from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, String

from .base import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    hash = Column(String(64), unique=True, nullable=False, index=True)
    is_signed = Column(Boolean, nullable=False)
    name = Column(String(60), nullable=False)
    fcm_token = Column(String(255))
    role = Column(Integer, nullable=False, default=0)
