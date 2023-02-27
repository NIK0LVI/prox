from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional

from datetime import date


class EmployeeSchema(BaseModel):
    employee_id: UUID4
    last_name: str
    first_name: str
    education: str
    email: str
    office_id: Optional[str]
    address: str
    compensation: float
    employment_start: date
    employment_end: date

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    last_name: str
    first_name: str
    education: Optional[str] = None
    email: str
    office_id: Optional[str] = None
    address: str
    compensation: float
    employment_start: date
    employment_end: date

    class Config:
        orm_mode = True
