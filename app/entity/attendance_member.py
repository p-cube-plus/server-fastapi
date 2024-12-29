from sqlalchemy import BigInteger, Column, Integer, String, Time

from .base import BaseEntity


class AttendanceMemberEntity(BaseEntity):
    __tablename__ = "attendance_member"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    attendance_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    state = Column(Integer, nullable=True, comment="출석, 지각, 불참")
    first_auth_time = Column(Time, nullable=True)
    second_auth_time = Column(Time, nullable=True)
