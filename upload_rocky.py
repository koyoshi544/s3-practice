# rocky802のバックアップをS3にアップロード
# 
from dotenv import load_dotenv
import os
import boto3
   
load_dotenv()

s3_file_path = 'rocky802_20250214.tar.xz'
s3_bucket_name = 'fsgtests3'
local_file_path = '/tmp/rocky802_20250214.tar.xz'

s3_client = boto3.client('s3')
s3_client.upload_file(local_file_path, s3_bucket_name, s3_file_path)

