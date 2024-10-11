from datetime import datetime, timezone

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# from app.core.exception import DomainException, UseCaseException

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_datetime = datetime.now(timezone.utc)
        print("api start")
        try:
            response: Response = await call_next(request)
        # except DomainException as e:
        #     response = JSONResponse(
        #         status_code=e.status_code(),
        #         content={"detail": e.message()},
        #     )
        # except UseCaseException as e:
        #     response = JSONResponse(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content={"detail": e.message()},
        #     )
        except Exception as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "detail": {
                        "description": f"{e}",
                    },
                },
            )
        end_datetime = datetime.now(timezone.utc)
        process_time = end_datetime - start_datetime
        print(process_time)
        print(request.url)
        print(response)
        print("log http")
        return response
