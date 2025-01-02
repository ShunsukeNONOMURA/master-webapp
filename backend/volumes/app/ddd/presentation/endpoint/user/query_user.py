from fastapi import Depends
from sqlmodel import Session

from app.ddd.application.dto.user import QueryUserInputDTO, QueryUserOutputDTO
from app.ddd.application.usecase.user import QueryUserUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user.router import router
from app.ddd.presentation.schema.user import QueryUserRequest, QueryUserResponse


def __usecase(session: Session = Depends(get_session)) -> QueryUserUseCase:
    return QueryUserUseCase(uow=UserUnitOfWorkImpl(session))


@router.post(
    path="/query/users",
    response_model=QueryUserResponse
)
def query_user(
    request: QueryUserRequest,
    usecase: QueryUserUseCase = Depends(__usecase),
) -> QueryUserResponse:
    """Userをクエリする."""
    input_dto: QueryUserInputDTO = QueryUserInputDTO.model_validate(request)
    dto: QueryUserOutputDTO = usecase.execute(input_dto)
    return QueryUserResponse.model_validate(dto)
