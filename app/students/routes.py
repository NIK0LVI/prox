from datetime import date
from fastapi import APIRouter

from app.students.controller.student_controller import StudentController
from app.students.schemas.student_schemas import StudentSchema, StudentSchemaIn

from app.students.services.primitive_email_because_sendgrid_sucks import EmailNotifications

student_router = APIRouter(tags=["students"], prefix="/api/students")


@student_router.post("/add-new-student", response_model=StudentSchema)
def create_student(student: StudentSchemaIn):
    return StudentController.create_student(student.last_name,
                                            student.first_name,
                                            student.phone,
                                            student.address,
                                            student.city,
                                            student.postal,
                                            student.course_score,
                                            student.course_start,
                                            student.course_end)


@student_router.get("/student-id", response_model=StudentSchema)
def get_student_by_id(student_id: str):
    return StudentController.get_student_by_id(student_id)


@student_router.get("/student-last-name", response_model=StudentSchema)
def get_student_by_last_name(last_name: str):
    return StudentController.get_student_by_last_name(last_name)


@student_router.get("/get-all-students", response_model=list[StudentSchema])
def get_all_students():
    return StudentController.get_all_students()


@student_router.delete("/")
def delete_student_by_id(student_id: str):
    return StudentController.delete_student_by_ide(student_id)


@student_router.put("/update-student-by-id", response_model=StudentSchema)
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
    return StudentController.update_student(student_id, last_name, first_name, phone, address, city, postal,
                                            course_score, course_start, course_end)


@student_router.put("/email-notif")
def send_email(receiver_email):
    email = EmailNotifications(receiver_email)
    email_yeet = email.send_money_pls()
    return email_yeet
