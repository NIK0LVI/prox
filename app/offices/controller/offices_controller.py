from datetime import date
from fastapi import HTTPException, Response

from app.offices.exceptions import OfficeNotFoundException
from app.offices.services import OfficeServices


class OfficeController:
    @staticmethod
    def create_office(city, phone, address, postal):
        try:
            office = OfficeServices.create_office(city, phone, address, postal)

            return office
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_office_by_id(office_id: str):
        try:
            office = OfficeServices.get_office_by_id(office_id)
            if office:
                return office
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=500, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_office_by_address(address: str):
        try:
            office = OfficeServices.get_office_by_address(address)
            if office:
                return office
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_office(
            office_id: str,
            city: str = None,
            phone: str = None,
            address: str = None,
            postal: str = None
    ):
        try:
            office = OfficeServices.update_office(office_id, city, phone, address, postal)

            return office
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
