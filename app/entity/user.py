from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, String

from .base import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, index=True)
    hash = Column(String(64), unique=True, nullable=False, index=True)
    is_signed = Column(Boolean, nullable=False, default=False)
    name = Column(String(60), nullable=False)
    level = Column(Integer, nullable=False)
    grade = Column(Integer, nullable=False)
    part_index = Column(Integer, nullable=False)
    profile_image = Column(String(1023))
    univ = Column(String(100))
    last_cleaning = Column(Date)
    rest_type = Column(Integer, nullable=False)
    etc_message = Column(String(1023))
    absent_reason = Column(String(150))
    absent_detail_reason = Column(String(1023))
    phone_number = Column(String(56))
    join_date = Column(Date)
    birth_date = Column(Date)
    birth_month = Column(Integer)
    birth_day = Column(Integer)
    major = Column(String(256))
    student_id = Column(String(64))
    is_next_birth = Column(Boolean, nullable=False, default=False)
    return_plan_date = Column(Date)
    workshop_count = Column(Integer)
    gogoma = Column(String(30))
    warning_point = Column(Integer, nullable=False, default=0)
    fcm_token = Column(String(255))
    api_access_level = Column(Integer, nullable=False, default=0)
