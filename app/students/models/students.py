from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Date, Float, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class Student(Base):
    __tablename__ = "students"
    student_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    last_name = Column(String(100))
    first_name = Column(String(100))
    phone = Column(String(100))
    address = Column(String(100))
    city = Column(String(100))
    postal = Column(String(100))
    course_score = Column(Integer)
    course_start = Column(Date)
    course_end = Column(Date)

    def __init__(self, last_name, first_name, phone, address, city, postal, course_score, course_start, course_end):
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone
        self.address = address
        self.city = city
        self.postal = postal
        self.course_score = course_score
        self.course_start = course_start
        self.course_end = course_end

