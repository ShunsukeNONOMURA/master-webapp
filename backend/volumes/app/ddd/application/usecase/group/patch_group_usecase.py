from app.ddd.application.dto.group import PatchGroupInputDTO, PatchGroupOutputDTO
from app.ddd.application.usecase.group.base_group_usecase import BaseGroupUseCase
from app.ddd.domain import GroupId


class PatchGroupUseCase(BaseGroupUseCase[PatchGroupInputDTO, PatchGroupOutputDTO]):
    def execute(self, input_dto: PatchGroupInputDTO) -> PatchGroupOutputDTO:
        group_id = GroupId(root=input_dto.group_id)
        group = self._uow.group_repository.find_by_id(group_id)
        group.sqlmodel_update(input_dto.model_dump(exclude_unset=True))
        # hashed_password=create_hashed_password(str(group.group_password))
        # # print(hashed_password)
        # group.group_password = hashed_password
        # with self._uow:
        #     self._uow.group_repository.update(group)
        return PatchGroupOutputDTO.model_validate(group)
