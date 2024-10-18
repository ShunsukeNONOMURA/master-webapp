from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from fastapi import status
from app.core.exception import DomainException

class PermissionErrorException(DomainException):
    def __init__(self):
        super().__init__(
            error_code='010',
            status_code=status.HTTP_401_UNAUTHORIZED,
            description="実行権限がありません。",
        )

class AuthMiddleware(BaseHTTPMiddleware):
    def __check_permission(self) -> None:
        # raise PermissionErrorException
        return

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print("auth middleware")
        self.__check_permission()
        response: Response = await call_next(request)
        return response
