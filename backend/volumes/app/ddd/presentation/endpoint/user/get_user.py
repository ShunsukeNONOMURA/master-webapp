from fastapi import Depends, Path
from sqlmodel import Session

from app.ddd.application.dto.user import GetUserInputDTO, GetUserOutputDTO
from app.ddd.application.usecase.user import (
    # GetUsersUseCase,
    GetUserUseCase,
)
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import GetUsersUserResponse

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

# #######################
def __usecase(session: Session = Depends(get_session)) -> GetUserUseCase:
    return GetUserUseCase(uow=UserUnitOfWorkImpl(session))

################ me
@router.get(
    path="/users/me",
    response_model=GetUsersUserResponse,
)
def get_me(
    usecase: GetUserUseCase = Depends(__usecase),
    # jwt_payload: dict = Depends(get_jwt_payload),
) -> GetUsersUserResponse:
    """自身を取得する."""
    user_id = "guest" # jwt_payload.get("user_id")
    input_dto: GetUserInputDTO = GetUserInputDTO(user_id=user_id)
    dto: GetUserOutputDTO = usecase.execute(input_dto)
    return GetUsersUserResponse.model_validate(dto)

################ id
@router.get(
    path="/users/{userId}",
    response_model=GetUsersUserResponse,
)
def get_user(
    user_id: str = Path(..., alias="userId"),
    usecase: GetUserUseCase = Depends(__usecase),
) -> GetUsersUserResponse:
    """ユーザを取得する."""
    input_dto: GetUserInputDTO = GetUserInputDTO(user_id=user_id)
    dto: GetUserOutputDTO = usecase.execute(input_dto)
    return GetUsersUserResponse.model_validate(dto)

