from fastapi import APIRouter

from app.ddd.presentation.endpoint import (
    conversation,
    conversation_view,
    health,
    pages,
    users,
)

main_router = APIRouter()

main_router.include_router(health.router, tags=["/health"])
main_router.include_router(users.router, tags=["/users"])
main_router.include_router(conversation.router, tags=["/conversation"])
main_router.include_router(conversation_view.router)
main_router.include_router(pages.router, tags=["/pages"])
