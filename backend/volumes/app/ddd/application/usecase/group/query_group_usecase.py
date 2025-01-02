from app.ddd.application.dto.group import QueryGroupInputDTO, QueryGroupOutputDTO
from app.ddd.application.usecase.group.base_group_usecase import BaseGroupUseCase


class QueryGroupUseCase(BaseGroupUseCase[QueryGroupInputDTO, QueryGroupOutputDTO]):
    def execute(self, input_dto: QueryGroupInputDTO) -> QueryGroupOutputDTO:
        print(input_dto)
        groups = self._uow.group_repository.query()
        return QueryGroupOutputDTO(groups = groups)
