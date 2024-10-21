from sqlmodel import Field, SQLModel

class __BaseRequest(SQLModel):
    pass

class GetUsersRequest(__BaseRequest):
    pass