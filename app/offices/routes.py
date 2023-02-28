from datetime import date
from fastapi import APIRouter

from app.offices.controller.offices_controller import OfficeController
from app.offices.schemas.offices_schemas import OfficesSchema, OfficesSchemaIn

office_router = APIRouter(tags=["offices"], prefix="/api/offices")


@office_router.post("/add-new-office", response_model=OfficesSchema)
def create_office(office: OfficesSchemaIn):
    return OfficeController.create_office(office.city,
                                          office.phone,
                                          office.address,
                                          office.postal)


@office_router.get("/id", response_model=OfficesSchema)
def get_office_by_id(office_id: str):
    return OfficeController.get_office_by_id(office_id)


@office_router.get("/address", response_model=OfficesSchema)
def get_office_by_address(address: str):
    return OfficeController.get_office_by_address(address)


@office_router.put("/update-office", response_model=OfficesSchema)
def update_office(
        office_id: str,
        city: str = None,
        phone: str = None,
        address: str = None,
        postal: str = None
):
    return OfficeController.update_office(office_id, city, phone, address, postal)
