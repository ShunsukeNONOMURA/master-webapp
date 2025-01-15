from fastapi import APIRouter

from app.ddd.presentation.endpoint import group, health, page, token, user, user_report

# version = 'v1'
# main_router = APIRouter(prefix=f'/{version}') # バージョンの追記
main_router = APIRouter() # バージョンの追記

main_router.include_router(token.router, tags=["token"])
main_router.include_router(health.router, tags=["health"])
main_router.include_router(user.router, tags=["user"])
main_router.include_router(user_report.router, tags=["user-report"])
main_router.include_router(group.router, tags=["group"])
main_router.include_router(page.router, tags=["page"])
