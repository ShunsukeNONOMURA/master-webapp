from fastapi import Depends
from sqlmodel import Session

from app.ddd.application.dto.user import CreateUserInputDTO, CreateUserOutputDTO
from app.ddd.application.usecase.user import CreateUserUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import CreateUsersRequest, PostUsersResponse


def __usecase(session: Session = Depends(get_session)) -> CreateUserUseCase:
    return CreateUserUseCase(uow=UserUnitOfWorkImpl(session))


@router.post(
    path="/users",
    response_model=PostUsersResponse
)
def create_users(
    request: CreateUsersRequest,
    usecase: CreateUserUseCase = Depends(__usecase),
) -> PostUsersResponse:
    """ユーザを作成する."""
    input_dto: CreateUserInputDTO = CreateUserInputDTO.model_validate(request)
    dto: CreateUserOutputDTO = usecase.execute(input_dto)
    return PostUsersResponse.model_validate(dto)
