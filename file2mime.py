import argparse
import mimetypes
from pathlib import Path

# argparse.ArgumentParserクラスをインスタンス化して、説明等を引数として渡す
parser = argparse.ArgumentParser(
    prog="file2mime",  # プログラム名
    usage="python file2mime.py -f <file_name>", # プログラムの利用方法
    description="file name to MIME type", # ヘルプの前に表示
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
