


from sqlmodel import Field

from app.core.base import BaseRequest


class CreateUserReportRequest(BaseRequest):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: str = Field(default="99")
