from dotenv import load_dotenv
import os
import boto3

load_dotenv()

s3_bucket_name = 'fsgtests3'

s3_client = boto3.client('s3')
response = s3_client.list_objects_v2(Bucket=s3_bucket_name)
for obj in response['Contents']:
    print(obj['Key'])

