from fastapi import Depends, Path, status
from sqlmodel import Session

from app.ddd.application.dto.user import DeleteUserInputDTO, DeleteUserOutputDTO
from app.ddd.application.usecase.user import DeleteUserUseCase
from app.ddd.domain import UserNotFoundError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import DeleteUserResponse


def __usecase(session: Session = Depends(get_session)) -> DeleteUserUseCase:
    return DeleteUserUseCase(uow=UserUnitOfWorkImpl(session))

@router.delete(
    path="/users/{userId}",
    response_model=DeleteUserResponse,
    responses={
        # TODO(nonomura): Error 1:n ErrorResponse.errors
        # status.HTTP_404_NOT_FOUND: UserNotFoundError(user_id='dammy').response(),
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            UserNotFoundError(user_id="dammy").camel_detail(),
                        ]
                    }
                }
            },
        }
    },

)
def delete_user(
    user_id: str = Path(..., alias="userId"),
    usecase: DeleteUserUseCase = Depends(__usecase),
) -> DeleteUserResponse:
    """Userを削除する."""
    input_dto: DeleteUserInputDTO = DeleteUserInputDTO(user_id=user_id)
    dto: DeleteUserOutputDTO = usecase.execute(input_dto)
    return DeleteUserResponse.model_validate(dto)
