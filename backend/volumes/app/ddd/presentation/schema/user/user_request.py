

from datetime import datetime
from typing import Any

from pydantic import validator
from sqlmodel import Field

from app.core.base import BaseRequest
from app.ddd.infrastructure.util.convert import recursive_to_snake


class CreateUserRequest(BaseRequest):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: str = Field(default="99")

class PatchUsersRequest(BaseRequest):
    updated_at: datetime # 楽観的ロック用途
    user_password: str | None = Field(None)
    user_name: str | None = Field(None)
    user_role_code: str | None = Field(None)

_filters_example = {
    "userId": "guest",
}

class QueryUsersRequest(BaseRequest):
    offset: int = Field(default="0")
    limit: int = Field(default="10")
    query: dict[str,Any] = Field(default=_filters_example)

    @validator("query", pre=True, always=True)
    def validate_query(cls, query: dict[str, Any]) -> dict[str, Any]:
        """filtersのcaseをスネークに変換する."""
        return recursive_to_snake(query)
