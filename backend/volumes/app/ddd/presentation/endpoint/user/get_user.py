from typing import Any

from fastapi import Depends, Path, status

# def __t_usecase(session: Session = Depends(get_session)) -> GetUsersUseCase:
#     user_repository = UserRepository(session)
#     return GetUsersUseCase(user_repository)
# @router.get(
#     path="/users",
#     # response_model=GetUsersResponse,
# )
# def get_users(
#     usecase: GetUsersUseCase = Depends(__t_usecase),
# ):
#     """ユーザを一覧する."""
#     dto : GetUserOutputDTO = usecase.execute()
#     return dto
from sqlmodel import Session

from app.core.depends.jwt_data_depends import jwt_data_depends
from app.ddd.application.dto.user import GetUserInputDTO, GetUserOutputDTO
from app.ddd.application.usecase.user import (
    # GetUsersUseCase,
    GetUserUseCase,
)
from app.ddd.domain import UserNotFoundError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import GetUserResponse


# #######################
def __usecase(session: Session = Depends(get_session)) -> GetUserUseCase:
    return GetUserUseCase(uow=UserUnitOfWorkImpl(session))

################ me
@router.get(
    path="/users/me",
    response_model=GetUserResponse,
)
def get_me(
    usecase: GetUserUseCase = Depends(__usecase),
    jwt_data: dict[str, Any] = Depends(jwt_data_depends),
) -> GetUserResponse:
    """自身を取得する."""
    input_dto: GetUserInputDTO = GetUserInputDTO(user_id=jwt_data["sub"])
    # input_dto: GetUserInputDTO = GetUserInputDTO(user_id="guest")
    dto: GetUserOutputDTO = usecase.execute(input_dto)
    return GetUserResponse.model_validate(dto)

################ id
@router.get(
    path="/users/{userId}",
    response_model=GetUserResponse,
    responses={
        status.HTTP_404_NOT_FOUND: UserNotFoundError(user_id="dammy").response(),
    },
)
def get_user(
    user_id: str = Path(..., alias="userId"),
    usecase: GetUserUseCase = Depends(__usecase),
) -> GetUserResponse:
    """ユーザを取得する."""
    input_dto: GetUserInputDTO = GetUserInputDTO(user_id=user_id)
    dto: GetUserOutputDTO = usecase.execute(input_dto)
    return GetUserResponse.model_validate(dto)


