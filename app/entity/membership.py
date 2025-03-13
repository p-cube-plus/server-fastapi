from sqlalchemy import BigInteger, Column, Date, Integer

from .base import BaseEntity


class MembershipEntity(BaseEntity):
    __tablename__ = "membership"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True, index=True)
    level = Column(Integer, nullable=False)
    part = Column(Integer, nullable=False)
    join_date = Column(Date, nullable=True)
