from app.core.abstract.ddd import BaseUsecase
from app.ddd.application.schema.user import DeleteUserParam, DeleteUserDto
from app.ddd.infra.repository.user_repository import UserRepository

from app.ddd.domain.user import UserId

class DeleteUserUseCase(BaseUsecase):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, param: DeleteUserParam) -> DeleteUserDto:
        user_id: UserId = UserId(root=param.user_id)
        # user_id: UserId = UserId.model_validate(param.user_id)
        user_id = self.__user_repository.delete(user_id)
        return DeleteUserDto(user_id=user_id.root)
