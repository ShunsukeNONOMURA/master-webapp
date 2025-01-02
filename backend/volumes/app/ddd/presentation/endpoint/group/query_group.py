from fastapi import Depends
from sqlmodel import Session

from app.ddd.application.dto.group import QueryGroupInputDTO, QueryGroupOutputDTO
from app.ddd.application.usecase.group import QueryGroupUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import GroupUnitOfWorkImpl
from app.ddd.presentation.endpoint.group.router import router
from app.ddd.presentation.schema.group import QueryGroupRequest, QueryGroupResponse


def __usecase(session: Session = Depends(get_session)) -> QueryGroupUseCase:
    return QueryGroupUseCase(uow=GroupUnitOfWorkImpl(session))


@router.post(
    path="/query/groups",
    response_model=QueryGroupResponse
)
def query_group(
    request: QueryGroupRequest,
    usecase: QueryGroupUseCase = Depends(__usecase),
) -> QueryGroupResponse:
    """Userをクエリする."""
    input_dto: QueryGroupInputDTO = QueryGroupInputDTO.model_validate(request)
    dto: QueryGroupOutputDTO = usecase.execute(input_dto)
    return QueryGroupResponse.model_validate(dto)
