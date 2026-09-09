# ファイルをS3にアップロード（ContentTypeを指定）
# 
from dotenv import load_dotenv
import os
import boto3
import argparse
import mimetypes
from pathlib import Path

def main():
    load_dotenv()

    # argparse.ArgumentParserクラスをインスタンス化して、説明等を引数として渡す
    parser = argparse.ArgumentParser(
        prog="upload_ws3",  # プログラム名
        usage="python upload_ws3.py -f <file_name>", # プログラムの利用方法
        description="ファイルをAmazon S3にアップロード", # ヘルプの前に表示
        epilog="end", # ヘルプの後に表示
        add_help=True, # -h/–-helpオプションの追加
    )

    # 引数の設定
    parser.add_argument("-f", "--file", type=str, help="ファイル名")
    parser.add_argument("-t", "--type", type=str, default="auto", help="MIMEタイプ")

    # 引数の解析
    args = parser.parse_args()

    file_path = Path(args.file)
    file_name = file_path.name
    mime_type = args.type

    mimetypes.init()
    if mime_type == "auto":
        mime_type = mimetypes.guess_type(file_name)[0]

    if mime_type is None:
        print("MIMEタイプが推定できません。-t パラメータで指定してください。")
    else:
        print(f"File path: {file_path}")
        print(f"File name: {file_name}")
        print(f"MIME type: {mime_type}")
        upload_ws3(file_path, file_name, mime_type)

def upload_ws3(src, dest, type):
    # 設定値
    s3_file_path = dest
    s3_bucket_name = 'ws3aclewm1il9xopvli7'
    local_file_path = src
    content_type = type

    # 実行内容
    s3 = boto3.resource('s3')
    with open(local_file_path, 'rb') as body_file:
        response = s3.Bucket(s3_bucket_name).put_object(Key = s3_file_path, Body = body_file, ContentType = content_type)

if __name__ == '__main__':  
    main()
