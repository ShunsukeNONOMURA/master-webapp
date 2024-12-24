from datetime import datetime
from enum import Enum, unique

from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel
from sqlmodel._compat import SQLModelConfig

from app.core.base import BaseValueObject


@unique
class UserRoleEnum(str, Enum):
    Admin = "00"
    General = "10"
    Guest = "99"

class UserId(BaseValueObject, frozen=True):
    root: str

class User(SQLModel):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: UserRoleEnum
    # user_role_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    # def _id(self) -> str:
    #     return self.user_id

    # def update(self, updates: dict[str, Any]) -> None:
    #     # TODO(nonomura): mixinにするか検討
    #     for key, value in updates.items():
    #         if value is not None:  # 値がNoneでない場合のみ更新
    #             print(value)
    #             print(type(value))
    #             setattr(self, key, value)

    model_config = SQLModelConfig(
        populate_by_name=True,
        alias_generator=to_camel,
    )

