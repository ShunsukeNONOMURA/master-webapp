from app.core.base import BaseRequest


class CreateTokenRequest(BaseRequest):
    user_id: str
    user_password: str
