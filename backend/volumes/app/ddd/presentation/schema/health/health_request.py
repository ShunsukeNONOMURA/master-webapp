from sqlmodel import SQLModel


class __BaseRequest(SQLModel):
    pass

class GetHealthRequest(__BaseRequest):
    pass
