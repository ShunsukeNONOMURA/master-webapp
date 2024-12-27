
# from pydantic import SecretStr


from datetime import datetime
from typing import Any

from sqlmodel import Field

from app.core.base import BaseInputDTO


class GetUserInputDTO(BaseInputDTO):
    user_id: str

class CreateUserInputDTO(BaseInputDTO):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: str

class PatchUserInputDTO(BaseInputDTO):
    user_id: str
    updated_at: datetime
    user_password: str | None = Field(None)
    user_name: str | None = Field(None)
    user_role_code: str | None = Field(None)

class DeleteUserInputDTO(BaseInputDTO):
    user_id: str

class QueryUserInputDTO(BaseInputDTO):
    offset: int
    limit: int
    query: dict[str, Any]
