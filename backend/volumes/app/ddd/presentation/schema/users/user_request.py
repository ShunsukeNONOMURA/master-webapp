
from app.core.abstract.ddd import BaseRequest

from pydantic import Field

from enum import Enum, unique
@unique
class UserRoleEnum(Enum):
    Admin = "00"
    General = "10"
    Guest = "99"


class PostUsersRequest(BaseRequest):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: UserRoleEnum = Field(default=None, example='10')
