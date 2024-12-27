from app.ddd.application.dto.user import QueryUserInputDTO, QueryUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase


class QueryUserUseCase(BaseUserUseCase[QueryUserInputDTO, QueryUserOutputDTO]):
    def execute(self, input_dto: QueryUserInputDTO) -> QueryUserOutputDTO:
        print(input_dto)
        users = self._uow.user_repository.query()
        return QueryUserOutputDTO(users = users)
