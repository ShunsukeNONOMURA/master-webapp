from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.base import BaseError
from app.ddd.infrastructure.util import recursive_to_camel


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response: Response = await call_next(request)
        except BaseError as e:
            print(e)
            print("on error")
            # TODO(nonomura): エラー設計後
            # response = JSONResponse(
            #     status_code=500,
            #     content={"detail": "An internal server error occurred."},
            # )
            # raise

            # response = e.detail().model_dump(by_alias=True)
            # print(response)
            response = JSONResponse(
                status_code=e.status_code(),
                # content={"detail": e.detail()},
                # content=e.detail(),
                content=recursive_to_camel(e.detail())
            )

        except Exception:
            raise # ハンドリングしない場合
        #     print(e)
        #     print("on error")
        #     # TODO(nonomura): エラー設計後
        #     response = JSONResponse(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         content={"detail": "An internal server error occurred."},
        #     )
        print(response)
        return response
