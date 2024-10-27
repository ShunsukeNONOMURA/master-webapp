from datetime import datetime, timezone

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# from app.core.exception import DomainException, UseCaseException

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_datetime = datetime.now(timezone.utc)
        print("logging middleware : api start")

        response: Response = await call_next(request)

        # error handling 後を含めた実行について保存する

        end_datetime = datetime.now(timezone.utc)
        duration = end_datetime - start_datetime

        # ヘッダに情報をトレインケースで埋める
        # 後で分けると思う
        response.headers["X-Resource-Code"] = "RRR"
        response.headers["X-Action-Code"] = "A"
        response.headers["X-Error-Code"] = "EEE"

        # exception_handling_middlewareでX-Error-Codeは設定する
        response.headers["X-Result-Code"] = "S" + response.headers["X-Resource-Code"] + response.headers["X-Action-Code"]  + response.headers["X-Error-Code"]
        response.headers["X-Response-Time"] = str(duration)


        # レスポンスについてのログを残す
        print("log info")
        print(request.url)
        print(response.status_code)
        print(f"route response headers: {response.headers}")

        return response
