from app.db.database import SessionLocal
from app.offices.repository.offices_repository import OfficeRepository


class OfficeServices:
    @staticmethod
    def create_office(city, phone, address, postal):
        with SessionLocal() as db:
            try:
                office_repo = OfficeRepository
                return office_repo.create_office(city=city, phone=phone, address=address, postal=postal)
            except Exception as e:
                raise e

    @staticmethod
    def get_office_by_id(office_id: str):
        try:
            with SessionLocal() as db:
                office_repo = OfficeRepository(db)
                return office_repo.get_office_by_id(office_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_office_by_address(address: str):
        try:
            with SessionLocal() as db:
                office_repo = OfficeRepository(db)
                return office_repo.get_office_by_address(address)
        except Exception as e:
            raise e

    @staticmethod
    def update_office(
            office_id: str,
            city: str = None,
            phone: str = None,
            address: str = None,
            postal: str = None
    ):
        try:
            with SessionLocal() as db:
                office_repo = OfficeRepository(db)
                return office_repo.update_office(office_id, city, phone, address, postal)

        except Exception as e:
            raise e
