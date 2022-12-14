import boto3

from fastapi import APIRouter
from boto3.dynamodb.conditions import Key


from vehicle_app.routers.mock_data import vehicles
from vehicle_app.models.api_params import GetVehicles
from vehicle_app.aws_connect import dynamodb_connect

router = APIRouter()


@router.get("/vehicles", tags=['vehicles'])
async def get_all_vehicles():

    vehicle_data: GetVehicles = vehicles
    # result = dynamodb_connect().get_item(TableName="vehicles", Key={"vehicle_id": {"N": "101"}})
    # print(result)
    # results = dynamodb_connect().query(KeyConditionExpression=Key("vehicle_id").eq(1))
    # print("Check 82", results)

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1",
                              aws_access_key_id='AKIAXLNLFD5Q3G6FUDGG',
                              aws_secret_access_key='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')
    table = dynamodb.Table("vehicles")
    response = table.query(KeyConditionExpression="vehicle_id")

    print("Check 83", response)


    # return {'vehicles': vehicle_data}
    return response

@router.get("/vehcles/{vehicle_name}", tags=['vehicles'])
async def get_vehicle(vehicle_name:str):

    return {'vehicle': vehicle_name}