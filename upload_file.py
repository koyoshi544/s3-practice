from dotenv import load_dotenv
import os
import boto3
   
load_dotenv()

s3_file_path = 'boto3_test.txt'
s3_bucket_name = 'fsgtests3'
local_file_path = './boto3_test.txt'

s3_client = boto3.client('s3')
s3_client.upload_file(local_file_path, s3_bucket_name, s3_file_path)

