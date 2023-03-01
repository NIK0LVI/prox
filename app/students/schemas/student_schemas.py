from pydantic import BaseModel, UUID4
from typing import Optional

from datetime import date


class StudentSchema(BaseModel):
    student_id: UUID4
    last_name: str
    first_name: str
    phone: Optional[str]
    address: str
    city: str
    postal: str
    course_score: Optional[int]
    course_start: date
    course_end: Optional[date]

    class Config:
        orm_mode = True


class StudentSchemaIn(BaseModel):
    last_name: str
    first_name: str
    phone: Optional[str] = None
    address: str
    city: str
    postal: str
    course_score: Optional[int] = None
    course_start: date
    course_end: Optional[date] = None

    class Config:
        orm_mode = True
