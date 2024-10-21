from datetime import date

from sqlmodel import Field, SQLModel

class __BaseResponse(SQLModel):
    user_id: str = Field()
    user_password: str = Field()
    user_name: str = Field()
    user_role_code: str = Field()
    user_role_name: str = Field()
    user_creation_datetime: str = Field()
    user_update_datetime: str = Field()

class PostUsersResponse(__BaseResponse):
    pass

class GetUsersUserResponse(__BaseResponse):
    pass

class DeleteUsersResponse(__BaseResponse):
    user_id: str = Field()