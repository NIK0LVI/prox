from datetime import date
from fastapi import APIRouter, Depends

from app.employees.controller.employee_controller import EmployeeController

from app.employees.schemas.employee_schema import EmployeeSchema, EmployeeSchemaIn

employee_router = APIRouter(tags=["employees"], prefix="/api/employees")

""" Placeholder for login router. """


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.last_name,
                                              employee.first_name,
                                              employee.email,
                                              employee.address,
                                              employee.education,
                                              employee.compensation,
                                              employee.employment_start,
                                              employment_end=None)


@employee_router.get("/id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id)
