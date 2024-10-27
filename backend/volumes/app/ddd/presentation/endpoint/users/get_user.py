from fastapi import Path, Depends
from sqlmodel import Session



from app.ddd.application.schema.user import GetUserParam, GetUserDto

from app.ddd.application.usecase.user import (
    GetUsersUseCase,
    GetUserUseCase,
)

from app.ddd.presentation.endpoint.users.router import router
from app.ddd.presentation.schema.users import GetUsersUserResponse

from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.infra.database.db import get_session

def __t_usecase(session: Session = Depends(get_session)) -> GetUsersUseCase:
    user_repository = UserRepository(session)
    return GetUsersUseCase(user_repository)

@router.get(
    path="/users",
    # response_model=GetUsersResponse,
)
def get_users(
    usecase: GetUsersUseCase = Depends(__t_usecase),
):
    dto : GetUserDto = usecase.execute()
    return dto

################

def __usecase(session: Session = Depends(get_session)) -> GetUserUseCase:
    user_repository = UserRepository(session)
    return GetUserUseCase(user_repository)

@router.get(
    path="/users/{userId}",
    response_model=GetUsersUserResponse,
)
def get_user(
    user_id: str = Path(..., alias="userId"),
    usecase: GetUserUseCase = Depends(__usecase),
):
    param: GetUserParam = GetUserParam(user_id=user_id)
    dto: GetUserDto = usecase.execute(param)
    # return GetUsersUserResponse.model_validate(dto)
    return GetUsersUserResponse.model_validate(dto)
