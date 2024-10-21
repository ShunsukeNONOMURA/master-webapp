from datetime import date, datetime

from sqlmodel import SQLModel


class __BaseDto(SQLModel):
    msg: str

class GetHealthDto(__BaseDto):
    pass