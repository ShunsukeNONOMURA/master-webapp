from datetime import datetime
from enum import Enum, unique

from pydantic import SecretStr

from app.core.base import BaseEntity, BaseValueObject


@unique
class UserRoleEnum(str, Enum):
    Admin = "00"
    General = "10"
    Guest = "99"

class UserId(BaseValueObject, frozen=True):
    root: str

class User(BaseEntity):
    user_id: str
    user_password: SecretStr
    user_name: str
    user_role_code: UserRoleEnum
    # user_role_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def _id(self) -> str:
        return self.user_id
