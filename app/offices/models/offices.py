from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class Offices(Base):
    __tablename__ = "offices"
    office_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    city = Column(String(50), nullable=False, unique=True)
    phone = Column(String(50))
    address = Column(String(50))
    postal = Column(String(50))

    def __init__(self, city: str, phone: str, address: str, postal: str):
        self.city = city
        self.phone = phone
        self.address = address
        self.postal = postal
