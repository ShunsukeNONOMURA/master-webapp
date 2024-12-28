from datetime import UTC, datetime

# from app.core.exception import DomainException, UseCaseException
from logging import getLogger

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# handler_format = Formatter('%(levelname)s:     %(asctime)s - %(name)s - %(message)s')

# stream_handler = StreamHandler()
# stream_handler.setFormatter(handler_format)

logger = getLogger("main").getChild("logging_middleware")
# logger.setLevel(DEBUG)
# logger.addHandler(stream_handler)



class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_datetime = datetime.now(UTC)
        print("logging middleware : api start")

        response: Response = await call_next(request)


        # error handling 後を含めた実行について保存する

        end_datetime = datetime.now(UTC)
        duration = end_datetime - start_datetime

        # ヘッダに情報をトレインケースで埋める
        # 後で分けると思う
        response.headers["X-Resource-Code"] = "RRR"
        response.headers["X-Action-Code"] = "A"
        response.headers["X-Error-Code"] = "EEE"

        # exception_handling_middlewareでX-Error-Codeは設定する
        response.headers["X-Result-Code"] = "S" + response.headers["X-Resource-Code"] + response.headers["X-Action-Code"]  + response.headers["X-Error-Code"]

        # 時間に関する記載
        response.headers["X-Response-Start-Datetime"] = str(start_datetime)
        response.headers["X-Response-End-Datetime"] = str(end_datetime)
        response.headers["X-Response-Time"] = str(duration)


        # レスポンスについてのシステムログを残す
        logger.info("info")
        logger.warning("warn")
        logger.debug("debug")
        print(request.url)
        print(response.status_code)
        print(f"route response headers: {response.headers}")

        return response
