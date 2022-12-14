import boto3


def dynamodb_connect():
    dynamodb_client = boto3.client('dynamodb',
                                     region_name='us-east-1',
                                     aws_access_key_id='AKIAXLNLFD5Q3G6FUDGG',
                                     aws_secret_access_key='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')

    return dynamodb_client

