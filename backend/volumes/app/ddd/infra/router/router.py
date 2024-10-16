from fastapi import APIRouter

from app.ddd.presentation.endpoint import *


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler

main_router = APIRouter(route_class=TimedRoute)

main_router.include_router(health_view.router)
main_router.include_router(user_view.router)
main_router.include_router(conversation_view.router)
