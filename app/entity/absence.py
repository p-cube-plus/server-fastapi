from sqlalchemy import BigInteger, Column, Date, Integer, String

from .base import BaseEntity


class AbsenceEntity(BaseEntity):
    __tablename__ = "absence"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True, index=True)
    type = Column(Integer, nullable=False)  # 0: 재학, 1: 일반휴학, 2: 군휴학
    reason = Column(String(150), nullable=True)
    description = Column(String(1023), nullable=True)
    expected_return_date = Column(Date, nullable=True)
