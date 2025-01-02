from app.ddd.application.dto.group import CreateGroupInputDTO, CreateGroupOutputDTO
from app.ddd.application.usecase.group.base_group_usecase import BaseGroupUseCase
from app.ddd.domain.model import Group, GroupId


class CreateGroupUseCase(BaseGroupUseCase[CreateGroupInputDTO, CreateGroupOutputDTO]):
    def execute(self, input_dto: CreateGroupInputDTO) -> CreateGroupOutputDTO:
        print(input_dto)
        print("valid")
        group: Group = Group.model_validate(input_dto)
        print(group)
        with self._uow:
            self._uow.group_repository.insert(group)
            group_id = GroupId(root=group.group_id)
            group = self._uow.group_repository.find_by_id(group_id) # 更新情報を統合する
            return CreateGroupOutputDTO(group = group) # withの中でレスポンスを返す
