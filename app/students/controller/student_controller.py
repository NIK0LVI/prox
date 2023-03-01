from datetime import date
from fastapi import HTTPException, Response

from app.students.exceptions import *
from app.students.services import StudentServices


class StudentController:
    @staticmethod
    def create_student(last_name, first_name, phone, address, city, postal, course_score, course_start, course_end):
        try:
            student = StudentServices.create_student(last_name, first_name, phone, address, city, postal, course_score,
                                                     course_start, course_end)
            return student
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_student_by_id(student_id: str):
        try:
            student = StudentServices.get_student_by_id(student_id)
            if student:
                return student
        except StudentNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_student_by_last_name(last_name: str):
        try:
            student = StudentServices.get_student_by_last_name(last_name)
            if student:
                return student
        except StudentNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_students():
        student = StudentServices.get_all_students()
        return student

    @staticmethod
    def delete_student_by_ide(student_id: str):
        try:
            StudentServices.delete_student_by_id(student_id)
            return Response(content=f"Student with ID {student_id} deleted successfully. ")
        except StudentNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

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
            student = StudentServices.update_student(student_id, last_name, first_name, phone, address, city, postal,
                                                     course_score, course_start, course_end)
            return student
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
