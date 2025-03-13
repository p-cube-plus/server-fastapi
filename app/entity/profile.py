from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, String

from .base import BaseEntity


class ProfileEntity(BaseEntity):
    __tablename__ = "profile"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True, index=True)
    phone_number = Column(String(56), nullable=True)
    profile_image = Column(String(1023), nullable=True)
    birth_date = Column(Date, nullable=True)
    description = Column(String(1023), nullable=True)
