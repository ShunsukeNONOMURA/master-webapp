from sqlmodel import SQLModel


class __BaseRequest(SQLModel):
    pass

class PostConversationRequest(__BaseRequest):
    message: str
