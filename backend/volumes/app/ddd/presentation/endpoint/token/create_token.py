from fastapi import Depends
from fastapi.param_functions import Form
from sqlmodel import Session

from app.ddd.application.dto.token import CreateTokenInputDTO, CreateTokenOutputDTO
from app.ddd.application.usecase.token import CreateTokenUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.token.router import router
from app.ddd.presentation.schema.token import CreateTokenResponse


def __usecase(session: Session = Depends(get_session)) -> CreateTokenUseCase:
    return CreateTokenUseCase(uow=UserUnitOfWorkImpl(session))

@router.post(
    path="/token",
    response_model=CreateTokenResponse,
    # responses={
    #     status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
    # },
)
def create_token(
    user_id: str = Form(examples=["admin"], validation_alias="userId", alias="userId"),
    user_password: str = Form(examples=["admin"], validation_alias="userPassword", alias="userPassword"),
    usecase: CreateTokenUseCase = Depends(__usecase),
) -> CreateTokenResponse:
    """トークンを作成する."""
    input_dto: CreateTokenInputDTO = CreateTokenInputDTO(
        user_id = user_id,
        user_password = user_password
    )
    output_dto: CreateTokenOutputDTO = usecase.execute(input_dto)

    return CreateTokenResponse.model_validate(output_dto)
