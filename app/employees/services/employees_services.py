from datetime import date

from app.db.database import SessionLocal
from app.employees.repository.employee_repository import EmployeeRepository


class EmployeeServices:
    @staticmethod
    def create_employee(last_name, first_name, education, email, address, compensation, employment_start,
                        employment_end):
        with SessionLocal() as db:
            try:
                employee_repo = EmployeeRepository(db)
                return employee_repo.create_employee(last_name=last_name, first_name=first_name, education=education,
                                                     email=email, address=address, compensation=compensation,
                                                     employment_start=employment_start, employment_end=employment_end)
            except Exception as e:
                raise e

    @staticmethod
    def get_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repo = EmployeeRepository(db)
                return employee_repo.get_employee_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_employee_by_email(email: str):
        try:
            with SessionLocal() as db:
                employee_repo = EmployeeRepository(db)
                return employee_repo.get_employee_by_email(email)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_employees():
        try:
            with SessionLocal() as db:
                employee_repo = EmployeeRepository(db)
                return employee_repo.get_all_employees()
        except Exception as e:
            raise e

    @staticmethod
    def delete_employee_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repo = EmployeeRepository(db)
                employee_repo.delete_employee_by_id(employee_id)
                return True
        except Exception as e:
            raise e

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
            with SessionLocal() as db:
                employee_repo = EmployeeRepository(db)
                return employee_repo.update_employee(employee_id, last_name, first_name, education, email, address,
                                                     compensation, employment_start, employment_end)

        except Exception as e:
            raise e
