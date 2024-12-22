from sqlalchemy import BigInteger, Column, Integer, SmallInteger, String, Time

from .base import BaseEntity


class MeetingEntity(BaseEntity):
    __tablename__ = "meeting"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    type = Column(
        SmallInteger,
        nullable=False,
        comment="0 ~ 4 (정기, 디자인, 아트, 프로그래밍, 기타)",
    )
    title = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    day = Column(SmallInteger, nullable=False, comment="월요일: 0 ~ 일요일: 6")
    time = Column(Time, nullable=False)
