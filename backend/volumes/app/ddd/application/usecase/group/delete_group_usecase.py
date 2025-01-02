from app.ddd.application.dto.group import DeleteGroupInputDTO, DeleteGroupOutputDTO
from app.ddd.application.usecase.group.base_group_usecase import BaseGroupUseCase
from app.ddd.domain import GroupId


class DeleteGroupUseCase(BaseGroupUseCase[DeleteGroupInputDTO, DeleteGroupOutputDTO]):
    def execute(self, input_dto: DeleteGroupInputDTO) -> DeleteGroupOutputDTO:
        group_id: GroupId = GroupId(root=input_dto.group_id)
        with self._uow:
            self._uow.group_repository.delete(group_id)
        return DeleteGroupOutputDTO(group_id = group_id.root)
