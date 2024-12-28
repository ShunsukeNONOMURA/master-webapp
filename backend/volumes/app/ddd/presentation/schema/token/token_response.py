from pydantic import BaseModel, Field

# from app.core.base import BaseResponse

# class CreateTokenResponse(BaseResponse):
class CreateTokenResponse(BaseModel):
    """TODO(nonomura): case変換対応."""

    access_token: str
    token_type: str = Field(default="bearer")
