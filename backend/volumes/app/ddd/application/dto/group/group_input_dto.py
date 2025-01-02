
# from pydantic import SecretStr


from datetime import datetime
from typing import Any

from sqlmodel import Field

from app.core.base import BaseInputDTO


class GetGroupInputDTO(BaseInputDTO):
    group_id: str

class CreateGroupInputDTO(BaseInputDTO):
    group_responsible_user_id: str
    group_name: str

class PatchGroupInputDTO(BaseInputDTO):
    group_id: str
    updated_at: datetime
    group_password: str | None = Field(None)
    group_name: str | None = Field(None)
    group_role_code: str | None = Field(None)

class DeleteGroupInputDTO(BaseInputDTO):
    group_id: str

class QueryGroupInputDTO(BaseInputDTO):
    offset: int
    limit: int
    query: dict[str, Any]
