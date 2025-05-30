# ファイルをS3にアップロード（ContentTypeを指定）
# 
from dotenv import load_dotenv
import os
import boto3
   
load_dotenv()

# 設定値
s3_file_path = '20250423_kaigohoken.pdf'
s3_bucket_name = 'ws3aclewm1il9xopvli7'
local_file_path = '/tmp/20250423_介護保険認定結果通知書.pdf'
content_type = 'application/pdf'

# 実行内容
s3 = boto3.resource('s3')
with open(local_file_path, 'rb') as body_file:
    response = s3.Bucket(s3_bucket_name).put_object(Key = s3_file_path, Body = body_file, ContentType = content_type)
