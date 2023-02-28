from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.offices.exceptions import OfficeNotFoundException
from app.offices.models import Offices


class OfficeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_office(self, city, phone, address, postal):
        try:
            office = Offices(city=city, phone=phone, address=address, postal=postal)
            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except IntegrityError as e:
            raise e

    def get_office_by_id(self, office_id: str):
        office = self.db.query(Offices).filter(Offices.office_id).first()
        if office is None:
            raise OfficeNotFoundException(f"Office with ID {office_id} not found. ", 400)
        return office

    def get_office_by_address(self, address: str):
        office = self.db.query(Offices).filter(Offices.address == address).first()
        if office is None:
            raise OfficeNotFoundException(f"Office with the address {address} not found. ", 400)
        return office

    def update_office(self,
                      office_id: str,
                      city: str,
                      phone: str,
                      address: str,
                      postal: str
                      ):
        try:
            office = self.db.query(Offices).filter(Offices.office_id == office_id).first()
            if office is None:
                raise OfficeNotFoundException(f"Office with ID {office_id} not found. ", 400)
            if city is not None:
                office.city = city
            if phone is not None:
                office.phone = phone
            if address is not None:
                office.address = address
            if postal is not None:
                office.postal = postal

            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except Exception as e:
            raise e
