from datetime import date
from fastapi import APIRouter

from app.employees.controller.employee_controller import EmployeeController
from app.employees.schemas.employee_schema import EmployeeSchema, EmployeeSchemaIn

employee_router = APIRouter(tags=["employees"], prefix="/api/employees")


@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create_employee(employee.last_name,
                                              employee.first_name,
                                              employee.education,
                                              employee.email,
                                              employee.address,
                                              employee.compensation,
                                              employee.employment_start,
                                              employee.employment_end
                                              )


@employee_router.get("/employee-id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.get_employee_by_id(employee_id)


@employee_router.get("/employee-email", response_model=EmployeeSchema)
def get_employee_by_email(email: str):
    return EmployeeController.get_employee_by_email(email)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.get_all_employees()


@employee_router.delete("/")
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_employee_by_id(employee_id)


@employee_router.put("/update-employee-by-id", response_model=EmployeeSchema)
def update_employee(
        employee_id: str,
        last_name: str = None,
        first_name: str = None,
        education: str = None,
        email: str = None,
        address: str = None,
        compensation: float = None,
        employment_start: date = None,
        employment_end: date = None
):
    return EmployeeController.update_employee(employee_id, last_name, first_name, education, email, address,
                                              compensation, employment_start, employment_end)
