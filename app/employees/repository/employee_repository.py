from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.employees.exceptions import *
from app.employees.models import Employee

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db =db

    def create_employee(self, last_name, first_name, education, email, address, compensation, employment_start,
                 employment_end):
        try:
            employee = Employee(last_name=last_name, first_name=first_name, education=education, email=email,
                                address=address, compensation=compensation, employment_start=employment_start,
                                employment_end=employment_end)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_employee_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(f"Employee with employee ID {employee_id} not found. ", 400)
        return employee

    def get_employee_by_email(self, email: str):
        """ Raise an exception. """
        employee = self.db.query(Employee).filter(Employee.email == email).first()
        return employee

    def get_all_employees(self):
        employee = self.db.query(Employee).all()
        return employee

    def delete_employee_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with employee ID {employee_id} not found. ", 400)
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_employee(self,
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
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with employee ID {employee_id} not found. ", 400)
            if last_name is not None:
                employee.email = last_name
            if first_name is not None:
                employee.first_name = first_name
            if education is not None:
                employee.education = education
            if email is not None:
                employee.email = email
            if address is not None:
                employee.address = address
            if compensation is not None:
                employee.compensation = compensation
            if employment_start is not None:
                employee.employment_start = employment_start
            if employment_end is not None:
                employee.employment_end = employment_end

            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e



