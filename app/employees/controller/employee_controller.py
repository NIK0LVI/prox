from datetime import date
from fastapi import HTTPException, Response

from app.employees.exceptions import *
from app.employees.services import EmployeeServices


class EmployeeController:
    @staticmethod
    def create_employee(last_name, first_name, education, email, address, compensation, employment_start,
                        employment_end):
        try:
            employee = EmployeeServices.create_employee(last_name, first_name, education, email, address, compensation,
                                                        employment_start, employment_end)
            return employee
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            employee = EmployeeServices.get_employee_by_id(employee_id)
            if employee:
                return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_employees():
        employee = EmployeeServices.get_all_employees()
        return employee

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            EmployeeServices.delete_employee_by_id(employee_id)
            return Response(content=f"Employee with ID {employee_id} removed. ")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
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
        try:
            employee = EmployeeServices.update_employee(employee_id, last_name, first_name, education, email, address,
                                                        compensation, employment_start, employment_end)
            return employee
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
