from pydantic import BaseModel, UUID4
from typing import Optional

from datetime import date


class StudentSchema(BaseModel):
    student_id: UUID4
    last_name: str
    first_name: str
    phone: str
    address: str
    city: str
    postal: str
    course_score: int
    course_start: date
    course_end: date

    class Config:
        orm_mode = True


class StudentSchemaIn(BaseModel):
    last_name: str
    first_name: str
    phone: str
    address: str
    city: str
    postal: str
    course_score: int
    course_start: date
    course_end: date

    class Config:
        orm_mode = True
