# from fastapi import APIRouter

import time
from typing import Callable

from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute

from app.ddd.presentation.endpoint import (
    conversation_view,
    health,
    users,
)


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

main_router.include_router(health.router, tags=["/health"])
main_router.include_router(users.router, tags=["/users"])
main_router.include_router(conversation_view.router)
