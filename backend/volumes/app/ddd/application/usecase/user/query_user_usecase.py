from app.ddd.application.dto.user import QueryUserInputDTO, QueryUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase


class QueryUserUseCase(BaseUserUseCase[QueryUserInputDTO, QueryUserOutputDTO]):
    def execute(self, _: QueryUserInputDTO) -> QueryUserOutputDTO:
        users = self._uow.user_repository.query()
        return QueryUserOutputDTO(users = users)
