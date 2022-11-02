from pydantic import BaseModel, Field
from humps import camelize
from uuid import UUID


def to_camel(string):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class Vehicle(CamelModel):
    vehicle_id: UUID
    nickname: str
    make: str
    model: str
    trim: str
    year: int

