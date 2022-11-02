from fastapi import APIRouter

router = APIRouter()

@router.get("/vehicles", tags=['vehicles'])
async def get_all_vehicles():


    return {'vehicles': ['discover', 'pulsar', 'oddessey']}

@router.get("/vehcles/{vehicle_name}", tags=['vehicles'])
async def get_vehicle(vehicle_name:str):

    return {'vehicle': vehicle_name}