from fastapi import APIRouter

from vehicle_app.routers.mock_data import vehicles
from vehicle_app.models.api_params import GetVehicles

router = APIRouter()



@router.get("/vehicles", tags=['vehicles'], response_model=GetVehicles)
async def get_all_vehicles():

    vehicle_data: GetVehicles = vehicles
    return {'vehicles': vehicle_data}


@router.get("/vehcles/{vehicle_name}", tags=['vehicles'])
async def get_vehicle(vehicle_name:str):

    return {'vehicle': vehicle_name}