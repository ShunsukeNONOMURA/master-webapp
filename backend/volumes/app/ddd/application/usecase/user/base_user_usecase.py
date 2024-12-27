from app.core.base.base_usecase import (
    BaseInputDTOType,
    BaseOutputDTOType,
    BaseUsecase,
)
from app.ddd.application.uow import UserUnitOfWork


class BaseUserUseCase(BaseUsecase[BaseInputDTOType, BaseOutputDTOType]):
    def __init__(
            self,
            uow: UserUnitOfWork,
            # auth_payload,
        ) -> None:
        self._uow = uow
        # self._auth_payload = auth_payload



