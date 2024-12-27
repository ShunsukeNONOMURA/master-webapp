from fastapi import APIRouter

from app.ddd.presentation.endpoint import (
    health,
    page,
    user,
    user_report,
)

main_router = APIRouter()

main_router.include_router(health.router, tags=["health"])
main_router.include_router(user.router, tags=["user"])
main_router.include_router(user_report.router, tags=["user-report"])
main_router.include_router(page.router, tags=["page"])
