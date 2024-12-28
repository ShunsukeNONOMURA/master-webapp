from pydantic import Field

from app.core.base import BaseResponse


class CreateTokenResponse(BaseResponse):
    access_token: str
    token_type: str = Field(default="bearer")
