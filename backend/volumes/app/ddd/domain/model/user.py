# from app.ddd.domain.factory import UserReportFactory
import uuid
from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import Field

from app.core.base import BaseEntity, BaseValueObject
from app.ddd.domain import UserRoleEnum


class UserReport(BaseEntity):
    user_report_id: str = Field(default_factory=lambda: str(uuid.uuid4())) # デフォルトでアプリID採番
    title: str
    content: str
    created_user_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def _id(self) -> str:
        return self.user_report_id


class UserId(BaseValueObject):
    root: str

class User(BaseEntity):
    user_id: str
    # user_password: SecretStr
    user_password: str
    # hashed_password: str = Field("hogehoge")
    user_name: str
    user_role_code: UserRoleEnum
    # user_role_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    user_reports: list[UserReport] = Field([])

    def _id(self) -> str:
        return self.user_id

    def add_report(self, **kwargs: Mapping[str, Any]) -> UserReport:
        user_report = UserReport(
            created_user_id = self.user_id,
            **kwargs
        )
        self.user_reports.append(user_report)
        return user_report



