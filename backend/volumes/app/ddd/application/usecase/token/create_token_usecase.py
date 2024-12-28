from app.ddd.application.dto.token import CreateTokenInputDTO, CreateTokenOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain.model import Token, UserId


class CreateTokenUseCase(BaseUserUseCase[CreateTokenInputDTO, CreateTokenOutputDTO]):
    def execute(self, input_dto: CreateTokenInputDTO) -> CreateTokenOutputDTO:
        user_id = UserId(root=input_dto.user_id)
        user = self._uow.user_repository.find_by_id(user_id)


        self.auth_service.verify_password(
            plain_password = input_dto.user_password,
            hashed_password = user.user_password
        )


        token: Token = self.token_factory.create(
            user = user,
        )

        return CreateTokenOutputDTO.model_validate(token)
