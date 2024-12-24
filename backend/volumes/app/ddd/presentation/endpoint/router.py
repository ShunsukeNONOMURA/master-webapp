from fastapi import APIRouter

from app.ddd.presentation.endpoint import (
    health,
    pages,
    user,
)

main_router = APIRouter()

main_router.include_router(health.router, tags=["/health"])
main_router.include_router(user.router, tags=["/users"])
main_router.include_router(pages.router, tags=["/pages"])
