from fastapi import Path, Depends

from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.presentation.endpoint.users.router import router
from app.ddd.presentation.schema.users import PostUsersRequest, PostUsersResponse

from app.ddd.application.usecase.user import CreateUserUseCase
from app.ddd.application.schema.user import CreateUserDto, CreateUserParam

from sqlmodel import Session

from app.ddd.infra.database.db import get_session


def __usecase(session: Session = Depends(get_session)) -> CreateUserUseCase:
    user_repository = UserRepository(session)
    return CreateUserUseCase(user_repository)

@router.post(
    path="/users",
    # response_model=PostUsersResponse
)
def post_users(
    request: PostUsersRequest,
    usecase: CreateUserUseCase = Depends(__usecase),
):
    param: CreateUserParam = CreateUserParam.model_validate(request)
    dto: CreateUserDto = usecase.execute(param)

    print(dto)
    return PostUsersResponse.model_validate(dto)
