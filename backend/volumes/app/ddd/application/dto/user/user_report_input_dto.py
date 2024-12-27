
# from pydantic import SecretStr




from app.core.base import BaseInputDTO


class CreateUserReportInputDTO(BaseInputDTO):
    title: str
    content: str
    user_id: str
