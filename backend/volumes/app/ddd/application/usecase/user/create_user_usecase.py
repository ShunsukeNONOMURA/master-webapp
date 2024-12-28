from app.ddd.application.dto.user import CreateUserInputDTO, CreateUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain.model import User
from app.ddd.infrastructure.auth.hash_password import create_hashed_password


class CreateUserUseCase(BaseUserUseCase[CreateUserInputDTO, CreateUserOutputDTO]):
    def execute(self, input_dto: CreateUserInputDTO) -> CreateUserOutputDTO:
        user: User = User.model_validate(input_dto)
        hashed_password=create_hashed_password(str(user.user_password))
        print(hashed_password)
        user.user_password = hashed_password
        with self._uow:
            self._uow.user_repository.insert(user)
        return CreateUserOutputDTO.model_validate(user)
