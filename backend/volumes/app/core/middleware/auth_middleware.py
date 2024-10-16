from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


def check_permission():
    return True

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print("auth")
        if check_permission():
            response: Response = await call_next(request)
        else:
            raise Exception # ログインサービスドメインエラー
        return response
