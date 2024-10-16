from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.exception import DomainException, UseCaseException


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response: Response = await call_next(request)
        except DomainException as e:
            response = JSONResponse(
                status_code=e.status_code(),
                content={"detail": e.message()},
            )
        except UseCaseException as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": e.message()},
            )
        except Exception as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "detail": {
                        "description": f"{e}",
                    },
                },
            )
        return response
