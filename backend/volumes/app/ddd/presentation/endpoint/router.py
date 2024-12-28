from fastapi import APIRouter

from app.ddd.presentation.endpoint import (
    health,
    page,
    token,
    user,
    user_report,
)

main_router = APIRouter()

main_router.include_router(token.router, tags=["token"])
main_router.include_router(health.router, tags=["health"])
main_router.include_router(user.router, tags=["user"])
main_router.include_router(user_report.router, tags=["user-report"])
main_router.include_router(page.router, tags=["page"])
