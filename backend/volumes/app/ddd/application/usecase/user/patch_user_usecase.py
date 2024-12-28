from app.ddd.application.dto.user import PatchUserInputDTO, PatchUserOutputDTO
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain import UserId
from app.ddd.infrastructure.auth.hash_password import create_hashed_password


class PatchUserUseCase(BaseUserUseCase[PatchUserInputDTO, PatchUserOutputDTO]):
    def execute(self, input_dto: PatchUserInputDTO) -> PatchUserOutputDTO:
        user_id = UserId(root=input_dto.user_id)
        user = self._uow.user_repository.find_by_id(user_id)
        user.sqlmodel_update(input_dto.model_dump(exclude_unset=True))
        hashed_password=create_hashed_password(str(user.user_password))
        # print(hashed_password)
        user.user_password = hashed_password
        with self._uow:
            self._uow.user_repository.update(user)
        return PatchUserOutputDTO.model_validate(user)
