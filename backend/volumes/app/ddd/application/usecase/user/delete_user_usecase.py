from app.ddd.infra.repository.user_repository import UserRepository

from app.ddd.application.schema.user import (
    GetUserDto
)


from app.core.abstract.ddd import (
    BaseUsecase
)

class DeleteUserUseCase(BaseUsecase):
    def __init__(self):
        self.__user_repository = UserRepository()

    def execute(self, user_id) -> GetUserDto:
        user = self.__user_repository.find_by_id(user_id)
        return GetUserDto(**user.to_dict())