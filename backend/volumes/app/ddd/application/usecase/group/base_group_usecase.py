from app.core.base.base_usecase import (
    BaseInputDTOType,
    BaseOutputDTOType,
    BaseUsecase,
)
from app.ddd.application.uow import GroupUnitOfWork

# from app.ddd.domain.factory import TokenFactory
# from app.ddd.domain.service import AuthService
# from app.ddd.infrastructure.factory import TokenFactoryImpl
# from app.ddd.infrastructure.service import AuthServiceImpl

# TOKEN_FACTORY = TokenFactoryImpl()
# AUTH_SERVICE = AuthServiceImpl()

class BaseGroupUseCase(BaseUsecase[BaseInputDTOType, BaseOutputDTOType]):
    def __init__(
            self,
            uow: GroupUnitOfWork,
            # auth_payload,
            # token_factory: TokenFactory = TOKEN_FACTORY,
            # auth_service: AuthService = AUTH_SERVICE,
        ) -> None:
        self._uow = uow
        # # self._auth_payload = auth_payload
        # self.token_factory = token_factory
        # self.auth_service = auth_service



