from datetime import datetime, timezone

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# from app.core.exception import DomainException, UseCaseException

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_datetime = datetime.now(timezone.utc)
        print("logging middleware : api start")

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
        duration = end_datetime - start_datetime
        response.headers["X-Response-Time"] = str(duration)

        print('log info')
        print(request.url)
        print(f"route response headers: {response.headers}")

        return response
