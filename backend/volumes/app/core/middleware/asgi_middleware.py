

# from app.core.exception import DomainException, UseCaseException
from starlette.types import ASGIApp, Receive, Scope, Send

# ws, http両方
class ASGIMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        print("asgi middleware")
        print(scope["type"])
        
        await self.app(scope, receive, send)
