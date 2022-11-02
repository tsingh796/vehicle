from pydantic import BaseModel
from uuid import UUID


class Vehicle(BaseModel):
    vehicle_id: UUID
    nickname: str
    make: str
    model: str
    trim: str
    year: int
