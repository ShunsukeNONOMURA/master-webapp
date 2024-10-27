from fastapi import Path, Depends
from sqlmodel import Session

from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.presentation.endpoint.users.router import router
from app.ddd.presentation.schema.users import DeleteUsersUserResponse

from app.ddd.application.schema.user import DeleteUserDto, DeleteUserParam

from app.ddd.application.usecase.user import DeleteUserUseCase

from app.ddd.infra.database.db import get_session

def __usecase(session: Session = Depends(get_session)) -> DeleteUserUseCase:
    user_repository = UserRepository(session)
    return DeleteUserUseCase(user_repository)

@router.delete(
    path="/users/{userId}",
    response_model=DeleteUsersUserResponse,
)
def delete_user(
    user_id: str = Path(..., alias="userId"),
    usecase: DeleteUserUseCase = Depends(__usecase),
):
    param: DeleteUserParam = DeleteUserParam(user_id=user_id)
    dto: DeleteUserDto = usecase.execute(param)
    return dto
