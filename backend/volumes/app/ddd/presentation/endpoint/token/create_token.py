

# from sqlmodel import Session
# from app.ddd.application.usecase.user import CreateUserUseCase
# from app.ddd.infrastructure.database.db import get_session
# from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
# def __usecase(session: Session = Depends(get_session)) -> CreateUserUseCase:
#     return CreateUserUseCase(uow=UserUnitOfWorkImpl(session))
from pydantic import BaseModel, Field

from app.ddd.presentation.endpoint.token.router import router


class Token(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")

# TOKEN_TYPE = "bearer"

@router.post(
    path="/token",
    # response_model=CreateUsersResponse,
    # responses={
    #     status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
    # },
)
def create_token(
    # request: CreateUserRequest,
    # usecase: CreateUserUseCase = Depends(__usecase),
    # form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """トークンを作成する."""
    # input_dto: CreateUserInputDTO = CreateUserInputDTO.model_validate(request)
    # dto: CreateUserOutputDTO = usecase.execute(input_dto)
    # return CreateUsersResponse.model_validate(dto)

    from app.ddd.infrastructure.auth import create_access_token
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": "guest"},
        # expires_delta=access_token_expires
    )
    return Token(
        access_token=access_token,
        # token_type=TOKEN_TYPE
    )
