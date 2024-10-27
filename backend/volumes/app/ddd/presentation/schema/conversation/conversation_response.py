
from typing import Any

from sqlmodel import Field

from app.core.abstract.ddd import BaseResponse


class PostConversationResponse(BaseResponse):
    event: str | None = Field(default=None)
    data: Any
