from fastapi import FastAPI

# CORSミドルウェア
from fastapi.middleware.cors import CORSMiddleware

# カスタムHTTPミドルウェア
from app.core.middleware import (
    ErrorHandlingMiddleware,
    LoggingMiddleware,
)
from app.ddd.presentation.endpoint import main_router

description = """
Webアプリのバックエンドのベースラインコード実装

## Health
- ヘルスの取得

## User
- ユーザの作成
- ユーザの取得
- ユーザの一覧
- ユーザの削除
"""

app = FastAPI(
    # description=description,
    # title='title', # APIに名前がある場合変更
    # version="1", # バージョンを記述する場合
    openapi_tags=[
        {
            "name": "health",
            "description": "ヘルスに関する操作。",
        },
        # {
        #     "name": "/token",
        #     "description": "トークンに関する操作",
        # },
        {
            "name": "user",
            "description": "ユーザーに関する操作。",
        },
        {
            "name": "user-report",
            "description": "ユーザーレポートに関する操作。",
        },
        # {
        #     "name": "/conversation",
        #     "description": "会話に関する操作。",
        # },
        # {
        #     "name": "/file",
        #     "description": "ファイルに関する操作。",
        # },
    ],
)

# CORSのオリジン
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# ミドルウェア登録（middlewareは逆順にコールされる）
app.add_middleware(ErrorHandlingMiddleware) # エラーハンドリングに関するミドルウェア
app.add_middleware(LoggingMiddleware) # ログに関するミドルウェア
app.add_middleware(
    CORSMiddleware, # CORSに関するミドルウェア
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(main_router)
