from app.ddd.application.dto.group import (
    GetGroupInputDTO,
    GetGroupOutputDTO,
)
from app.ddd.application.usecase.group.base_group_usecase import (
    BaseGroupUseCase,
)
from app.ddd.domain import Group, GroupId


class GetGroupUseCase(BaseGroupUseCase[GetGroupInputDTO, GetGroupOutputDTO]):
    def execute(self, input_dto: GetGroupInputDTO) -> GetGroupOutputDTO:
        group_id: GroupId = GroupId(root=input_dto.group_id)
        group: Group = self._uow.group_repository.find_by_id(group_id)
        return GetGroupOutputDTO(group = group)
