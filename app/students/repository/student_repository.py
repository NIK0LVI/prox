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

    def get_student_by_last_name(self, last_name: str):
        student = self.db.query(Student).filter(Student.last_name == last_name).first()
        if student is None:
            raise StudentNotFoundException(f"Student with last name {last_name} not found. ", 400)

    def get_all_students(self):
        student = self.db.query(Student).all()
        return student

    def delete_student_by_id(self, student_id: str):
        try:
            student = self.db.query(Student).filter(Student.student_id == student_id).first()
            if student is None:
                raise StudentNotFoundException(f"Student with student ID {student_id} not found. ", 400)
            self.db.delete(student)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_student(self,
                       student_id: str,
                       last_name: str = None,
                       first_name: str = None,
                       phone: str = None,
                       address: str = None,
                       city: str = None,
                       postal: str = None,
                       course_score: int = None,
                       course_start: date = None,
                       course_end: date = None
                       ):
        try:
            student = self.db.query(Student).filter(Student.student_id == student_id).first()
            if student is None:
                raise StudentNotFoundException(f"Student with student ID {student_id} not found. ", 400)
            if last_name is not None:
                student.last_name = last_name
            if first_name is not None:
                student.first_name = first_name
            if phone is not None:
                student.phone = phone
            if address is not None:
                student.address = address
            if city is not None:
                student.city = city
            if postal is not None:
                student.postal = postal
            if course_score is not None:
                student.course_score = postal
            if course_start is not None:
                student.course_start = course_start
            if course_end is not None:
                student.course_end = course_end

                self.db.add(student)
                self.db.commit()
                self.db.refresh(student)
                return student
        except Exception as e:
            raise e

"""proxy"""