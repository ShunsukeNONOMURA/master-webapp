from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response: Response = await call_next(request)
        except Exception as e:
            print(e)
            print("on error")
            # TODO(nonomura): エラー設計後
            # response = JSONResponse(
            #     status_code=500,
            #     content={"detail": "An internal server error occurred."},
            # )
            raise
        return response
