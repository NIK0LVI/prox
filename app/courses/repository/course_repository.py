from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.courses.exceptions import *
from app.courses.models import Courses


class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, start_date, end_date, level, comment, price):
        try:
            course = Courses(start_date=start_date, end_date=end_date, level=level,
                             comment=comment, price=price)
            self.db.add(course)
            self.db.commit()
            self.db.refresh(course)
            return course
        except IntegrityError as e:
            raise e
