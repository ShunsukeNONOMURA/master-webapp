from datetime import datetime

from pydantic import Field, SecretStr

from app.core.base import BaseEntity, BaseValueObject
from app.ddd.domain import UserRoleEnum


class UserReport(BaseEntity):
    user_report_id: str
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
    user_password: SecretStr
    # hashed_password: str = Field("hogehoge")
    user_name: str
    user_role_code: UserRoleEnum
    # user_role_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    user_reports: list[UserReport] = Field([])

    def _id(self) -> str:
        return self.user_id

    # def add_report(self, report: UserReport) -> None:
    #     self.user_reports.append(report)

