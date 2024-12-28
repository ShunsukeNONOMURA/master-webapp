
# from pydantic import SecretStr




from app.core.base import BaseInputDTO


class CreateTokenInputDTO(BaseInputDTO):
    user_id: str
    user_password: str
