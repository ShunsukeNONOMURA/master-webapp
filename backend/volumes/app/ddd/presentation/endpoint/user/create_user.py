from fastapi import Depends, status
from sqlmodel import Session

from app.ddd.application.dto.user import CreateUserInputDTO, CreateUserOutputDTO
from app.ddd.application.usecase.user import CreateUserUseCase
from app.ddd.domain import UserDuplicationError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import CreateUserRequest, CreateUserResponse


def __usecase(session: Session = Depends(get_session)) -> CreateUserUseCase:
    return CreateUserUseCase(uow=UserUnitOfWorkImpl(session))


@router.post(
    path="/users",
    response_model=CreateUserResponse,
    responses={
        status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
    },
)
def create_user(
    request: CreateUserRequest,
    usecase: CreateUserUseCase = Depends(__usecase),
) -> CreateUserResponse:
    """Userを作成する."""
    input_dto: CreateUserInputDTO = CreateUserInputDTO.model_validate(request)
    dto: CreateUserOutputDTO = usecase.execute(input_dto)
    return CreateUserResponse.model_validate(dto)
