from datetime import datetime

from pydantic import SecretStr
from sqlmodel import SQLModel


class __BaseDto(SQLModel):
    user_id: str
    user_password: SecretStr
    user_name: str
    user_role_code: str
    # user_role_name: str
    
    # user_creation_datetime: datetime
    # user_update_datetime: datetime

class GetUserDto(__BaseDto):
    pass

class CreateUserDto(__BaseDto):
    pass

class DeleteUserDto(SQLModel):
    user_id: str
