from fastapi import Depends, Path
from sqlmodel import Session

from app.ddd.application.dto.user import DeleteUserInputDTO, DeleteUserOutputDTO
from app.ddd.application.usecase.user import DeleteUserUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import DeleteUsersUserResponse


def __usecase(session: Session = Depends(get_session)) -> DeleteUserUseCase:
    return DeleteUserUseCase(uow=UserUnitOfWorkImpl(session))

@router.delete(
    path="/users/{userId}",
    response_model=DeleteUsersUserResponse,
)
def delete_user(
    user_id: str = Path(..., alias="userId"),
    usecase: DeleteUserUseCase = Depends(__usecase),
) -> DeleteUsersUserResponse:
    """ユーザを削除する."""
    input_dto: DeleteUserInputDTO = DeleteUserInputDTO(user_id=user_id)
    dto: DeleteUserOutputDTO = usecase.execute(input_dto)
    return DeleteUsersUserResponse.model_validate(dto)
