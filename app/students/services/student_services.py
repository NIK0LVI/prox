from datetime import date

from app.db.database import SessionLocal
from app.students.repository.student_repository import StudentRepository


class StudentServices:

    @staticmethod
    def create_student(last_name, first_name, phone, address, city, postal, course_score, course_start, course_end):
        with SessionLocal() as db:
            try:
                student_repo = StudentRepository(db)
                return student_repo.create_student(last_name=last_name, first_name=first_name, phone=phone,
                                                   address=address, city=city, postal=postal, course_score=course_score,
                                                   course_start=course_start, course_end=course_end)
            except Exception as e:
                raise e

    @staticmethod
    def get_student_by_id(student_id: str):
        try:
            with SessionLocal() as db:
                student_repo = StudentRepository(db)
                return student_repo.get_student_by_id(student_id)

        except Exception as e:
            raise e

    @staticmethod
    def get_student_by_last_name(last_name: str):
        try:
            with SessionLocal() as db:
                student_repo = StudentRepository(db)
                return student_repo.get_student_by_last_name(last_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_students():
        try:
            with SessionLocal() as db:
                student_repo = StudentRepository(db)
                return student_repo.get_all_students()
        except Exception as e:
            raise e

    @staticmethod
    def delete_student_by_id(student_id: str):
        try:
            with SessionLocal() as db:
                student_repo = StudentRepository(db)
                student_repo.delete_student_by_id(student_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update_student(
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
            with SessionLocal as db:
                student_repo = StudentRepository(db)
                return student_repo.update_student(student_id, last_name, first_name, phone, address, city, postal,
                                                   course_score, course_start, course_end)
        except Exception as e:
            raise e
