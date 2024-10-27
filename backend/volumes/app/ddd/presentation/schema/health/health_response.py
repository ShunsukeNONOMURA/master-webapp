
from sqlmodel import Field

from app.core.abstract.ddd import BaseResponse


class GetHealthResponse(BaseResponse):
    msg: str | None = Field(default=None)
