

from app.core.base import BaseResponse
from app.ddd.domain.model import User


class GetUsersUserResponse(BaseResponse):
    # user_id: str
    # user_password: SecretStr
    # user_name: str
    # user_role_code: str
    user: User

class PostUsersResponse(BaseResponse):
    user_id: str

class PatchUsersUserResponse(BaseResponse):
    user_id: str

class DeleteUsersUserResponse(BaseResponse):
    user_id: str

class QueryUsersResponse(BaseResponse):
    users: list[User]
