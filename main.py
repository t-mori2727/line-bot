import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からLINEのトークンを取得
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

if not LINE_CHANNEL_SECRET or not LINE_CHANNEL_ACCESS_TOKEN:
    raise ValueError("環境変数が正しく設定されていません。")
LINE_CHANNEL_SECRET = "xxx"
