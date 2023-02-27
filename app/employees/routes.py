from datetime import date
from fastapi import APIRouter, Depends

from app.employees.schemas.employee_schema import EmployeeSchema, EmployeeSchemaIn

employee_router = APIRouter(tags=["employees"], prefix="/api/employees")

""" Placeholder for login router. """


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    pass
