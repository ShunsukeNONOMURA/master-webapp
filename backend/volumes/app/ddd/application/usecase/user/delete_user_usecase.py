from app.ddd.application.dto.user import DeleteUserInputDTO, DeleteUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain import UserId


class DeleteUserUseCase(BaseUserUseCase[DeleteUserInputDTO, DeleteUserOutputDTO]):
    def execute(self, input_dto: DeleteUserInputDTO) -> DeleteUserOutputDTO:
        user_id: UserId = UserId(root=input_dto.user_id)
        with self._uow:
            self._uow.user_repository.delete(user_id)
        return DeleteUserOutputDTO(user_id = user_id.root)
