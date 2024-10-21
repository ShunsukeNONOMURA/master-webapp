from datetime import date

from sqlmodel import Field, SQLModel

class __BaseResponse(SQLModel):
    msg: str | None = Field(default=None)

class GetHealthResponse(__BaseResponse):
    pass