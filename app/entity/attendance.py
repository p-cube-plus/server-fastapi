from sqlalchemy import Column, Integer, Time

from .base import BaseEntity


class AttendanceEntity(BaseEntity):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    meeting_id = Column(Integer, nullable=False)
    first_auth_start_time = Column(Time, nullable=True)
    first_auth_end_time = Column(Time, nullable=True)
    second_auth_start_time = Column(Time, nullable=True)
    second_auth_end_time = Column(Time, nullable=True)
