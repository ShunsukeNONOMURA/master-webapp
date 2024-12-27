

from app.core.base import BaseResponse
from app.ddd.domain.model import User


class GetUserResponse(BaseResponse):
    # user_id: str
    # user_password: SecretStr
    # user_name: str
    # user_role_code: str
    user: User

class CreateUsersResponse(BaseResponse):
    user_id: str

class PatchUserResponse(BaseResponse):
    user_id: str

class DeleteUserResponse(BaseResponse):
    user_id: str

class QueryUsersResponse(BaseResponse):
    users: list[User]
