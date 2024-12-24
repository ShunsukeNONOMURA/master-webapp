from app.ddd.application.dto.user import CreateUserInputDTO, CreateUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain.model import User


class CreateUserUseCase(BaseUserUseCase[CreateUserInputDTO, CreateUserOutputDTO]):
    def execute(self, input_dto: CreateUserInputDTO) -> CreateUserOutputDTO:
        user: User = User.model_validate(input_dto)
        with self._uow:
            self._uow.user_repository.insert(user)
        return CreateUserOutputDTO.model_validate(user)
