from fastapi import Depends, Path, status
from sqlmodel import Session

from app.ddd.application.dto.user import PatchUserInputDTO, PatchUserOutputDTO
from app.ddd.application.usecase.user import PatchUserUseCase
from app.ddd.domain import UserNotFoundError, UserUpdateConflictError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import CreateUsersResponse, PatchUsersRequest


def __usecase(session: Session = Depends(get_session)) -> PatchUserUseCase:
    return PatchUserUseCase(uow=UserUnitOfWorkImpl(session))


@router.patch(
    path="/users/{userId}",
    response_model=CreateUsersResponse,
    responses={
        status.HTTP_404_NOT_FOUND: UserNotFoundError(user_id="dammy").response(),
        status.HTTP_409_CONFLICT: UserUpdateConflictError(user_id="dammy").response(),
    },
)
def patch_user(
    request: PatchUsersRequest,
    user_id: str = Path(..., alias="userId"),
    usecase: PatchUserUseCase = Depends(__usecase),
) -> CreateUsersResponse:
    """
    ユーザを更新する.

    更新しない場合、入力しない。
    """
    input_dto: PatchUserInputDTO = PatchUserInputDTO.model_validate({"user_id": user_id, **request.model_dump(exclude_unset=True)})
    dto: PatchUserOutputDTO = usecase.execute(input_dto)
    return CreateUsersResponse.model_validate(dto)
