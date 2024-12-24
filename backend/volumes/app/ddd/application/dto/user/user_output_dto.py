
from pydantic import SecretStr

from app.core.base import BaseOutputDTO
from app.ddd.domain import User


class BaseUserOutputDTO(BaseOutputDTO):
    user_id: str
    user_password: SecretStr
    user_name: str
    user_role_code: str
    # user_role_name: str

    # user_creation_datetime: datetime
    # user_update_datetime: datetime


class GetUserOutputDTO(BaseOutputDTO):
    user: User

class CreateUserOutputDTO(BaseUserOutputDTO):
    pass

class PatchUserOutputDTO(BaseUserOutputDTO):
    pass

class DeleteUserOutputDTO(BaseOutputDTO):
    user_id: str

class QueryUserOutputDTO(BaseOutputDTO):
    users: list[User]
