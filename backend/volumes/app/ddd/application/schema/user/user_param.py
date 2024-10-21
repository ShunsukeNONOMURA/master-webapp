from datetime import date, datetime

from sqlmodel import SQLModel


class __BaseDto(SQLModel):
    pass
    # user_id: str
    # user_password: str
    # user_name: str
    # user_role_code: str
    # user_role_name: str
    # user_creation_datetime: str
    # user_update_datetime: str

# class CreateStudentDto(__BaseDto):
#     pass


class GetUserParam(__BaseDto):
    pass