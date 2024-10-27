from datetime import datetime

from pydantic import Field, SecretStr
from sqlmodel import Field

from app.core.abstract.ddd import BaseResponse


class __BaseResponse(BaseResponse):
    user_id: str = Field()
    user_password: SecretStr = Field()
    user_name: str = Field()
    user_role_code: str = Field()
    # user_role_name: str = Field()

    # user_creation_datetime: datetime = Field()
    # user_update_datetime: datetime = Field()

class GetUsersUserResponse(__BaseResponse):
    pass

class PostUsersResponse(__BaseResponse):
    pass

class DeleteUsersUserResponse(BaseResponse):
    user_id: str = Field()
