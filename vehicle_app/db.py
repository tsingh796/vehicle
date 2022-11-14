import boto3

def dynamodb_connect():
    dynamodb_client = boto3.resource('dynamodb',
                                     region_name='',
                                     aws_access_key_id='',
                                     aws_secret_access_key='')
    return dynamodb_client