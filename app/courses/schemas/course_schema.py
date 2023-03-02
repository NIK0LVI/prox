from pydantic import BaseModel, UUID4
from typing import Optional

from datetime import date


class CourseSchema(BaseModel):
    course_id: UUID4
    start_date: date
    end_date: date
    level: str
    comment: Optional[str]
    price: float

    class Config:
        orm_mode = True


class CourseSchemaIn(BaseModel):
    start_date: date
    end_date: date
    level: str
    comment: Optional[str]
    price: float

    class Config:
        orm_mode = True
