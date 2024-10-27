
from sqlmodel import SQLModel

from pydantic import SecretStr

class __BaseDto(SQLModel):
    pass
    # user_id: str
    # user_password: str
    # user_name: str
    # user_role_code: str
    # user_role_name: str
    # user_creation_datetime: str
    # user_update_datetime: str

class GetUserParam(SQLModel):
    user_id: str

class CreateUserParam(SQLModel):
    user_id: str
    user_password: SecretStr
    user_name: str
    user_role_code: str

class DeleteUserParam(SQLModel):
    user_id: str
