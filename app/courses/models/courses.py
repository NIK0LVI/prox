from uuid import uuid4
from sqlalchemy import Column, String, Date, Float, TEXT

from app.db import Base


class Courses(Base):
    __tablename__ = "courses"
    course_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    start_date = Column(Date)
    end_date = Column(Date)
    level = Column(String(50))
    comment = Column(TEXT)
    price = Column(Float)

    def __init__(self, start_date, end_date, level, comment, price):
        self.start_date = start_date
        self.end_date = end_date
        self.level = level
        self.comment = comment
        self.price = price
        