from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.students.exceptions import *
from app.students.models import Student


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, last_name, first_name, phone, address, city, postal, course_score, course_start,
                       course_end):
        try:
            student = Student(last_name=last_name, first_name=first_name, phone=phone, address=address, city=city,
                              postal=postal, course_score=course_score, course_start=course_start,
                              course_end=course_end)
            self.db.add(student)
            self.db.commit()
            self.db.refresh(student)
            return student
        except IntegrityError as e:
            raise e

    def get_student_by_id(self, student_id: str):
        student = self.db.query(Student).filter(Student.student_id).first()
        if student is None:
            raise StudentNotFoundException(f"Student with student ID {student_id} not found. ", 400)
        return student
