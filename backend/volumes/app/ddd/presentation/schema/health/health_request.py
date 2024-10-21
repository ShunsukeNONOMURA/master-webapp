from sqlmodel import Field, SQLModel

class __BaseRequest(SQLModel):
    pass

class GetHealthRequest(__BaseRequest):
    pass