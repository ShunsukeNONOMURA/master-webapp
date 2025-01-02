# from app.ddd.domain.factory import UserReportFactory

import uuid
from datetime import datetime

from pydantic import Field

from app.core.base import BaseEntity, BaseValueObject
from app.ddd.domain.model.user import User


class GroupId(BaseValueObject):
    root: str

class Group(BaseEntity):
    group_id: str= Field(default_factory=lambda: str(uuid.uuid4())) # デフォルトでアプリID採番
    group_name: str

    group_responsible_user_id: str

    group_users: list[User] = Field(default=[])

    created_at: datetime | None = None
    updated_at: datetime | None = None

    # users: list[User] = Field([])

    def _id(self) -> str:
        return self.group_id

    # def add_report(self, **kwargs: Mapping[str, Any]) -> UserReport:
    #     user_report = UserReport(
    #         created_user_id = self.user_id,
    #         **kwargs
    #     )
    #     self.user_reports.append(user_report)
    #     return user_report



