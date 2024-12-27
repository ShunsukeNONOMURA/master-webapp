



from app.core.base import BaseRequest


class CreateUserReportRequest(BaseRequest):
    title: str
    content: str
