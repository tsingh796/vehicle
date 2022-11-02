from pydantic import BaseModel, Field
from typing import List

from vehicle_app.models.api_models import Vehicle


class GetVehicles(BaseModel):
    vehicles: List[Vehicle] = Field(description="List of all the vehicles")