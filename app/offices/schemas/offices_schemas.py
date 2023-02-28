from pydantic import BaseModel, UUID4


class OfficesSchema(BaseModel):
    office_id: UUID4
    city: str
    phone: str
    address: str
    postal: str

    class Config:
        orm_mode = True


class OfficesSchemaIn(BaseModel):
    city: str
    phone: str
    address: str
    postal: str

    class Config:
        orm_mode = True
