from app.ddd.application.dto.user import (
    GetUserInputDTO,
    GetUserOutputDTO,
)
from app.ddd.application.usecase.user.base_user_usecase import (
    BaseUserUseCase,
)
from app.ddd.domain import User, UserId


class GetUserUseCase(BaseUserUseCase[GetUserInputDTO, GetUserOutputDTO]):
    def execute(self, input_dto: GetUserInputDTO) -> GetUserOutputDTO:
        user_id: UserId = UserId(root=input_dto.user_id)
        user: User = self._uow.user_repository.find_by_id(user_id)
        print("pass")
        print(user.user_password)
        return GetUserOutputDTO(user = user)
