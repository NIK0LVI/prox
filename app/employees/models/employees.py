from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from app.db import Base


class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    last_name = Column(String(100))
    first_name = Column(String(100))
    education = Column(String(100))
    email = Column(String(100), unique=True)
    address = Column(String(50))
    compensation = Column(Float)
    employment_start = Column(Date)
    employment_end = Column(Date)

    # offices_office_id = Column(String(50), ForeignKey())
    # office = relationship("Office", lazy="subquery")

    def __init__(self, last_name, first_name, education, email, address, compensation, employment_start,
                 employment_end):
        self.last_name = last_name
        self.first_name = first_name
        self.education = education
        self.email = email
        self.address = address
        self.compensation = compensation
        self.employment_start = employment_start
        self.employment_end = employment_end
