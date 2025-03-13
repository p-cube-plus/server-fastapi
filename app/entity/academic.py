from sqlalchemy import BigInteger, Column, Integer, String

from .base import BaseEntity


class AcademicEntity(BaseEntity):
    __tablename__ = "academic"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True, index=True)
    university = Column(String(100), nullable=True)
    major = Column(String(256), nullable=True)
    grade = Column(Integer, nullable=False)
    student_id = Column(String(64), nullable=True)
