from fastapi import APIRouter

from app.ddd.presentation.endpoint import (
    conversation_view,
    health,
    users,
)

main_router = APIRouter()

main_router.include_router(health.router, tags=["/health"])
main_router.include_router(users.router, tags=["/users"])
main_router.include_router(conversation_view.router)
