

from datetime import datetime

from sqlmodel import Field

from app.core.base import BaseRequest


class CreateUsersRequest(BaseRequest):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: str = Field(default="99")

class PatchUsersRequest(BaseRequest):
    updated_at: datetime # 楽観的ロック用途
    user_password: str | None = Field(None)
    user_name: str | None = Field(None)
    user_role_code: str | None = Field(None)

class QueryUsersRequest(BaseRequest):
    pass
