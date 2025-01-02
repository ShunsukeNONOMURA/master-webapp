
from fastapi import Depends, Path, status
from sqlmodel import Session

from app.ddd.application.dto.group import GetGroupInputDTO, GetGroupOutputDTO
from app.ddd.application.usecase.group import (
    # GetGroupsUseCase,
    GetGroupUseCase,
)
from app.ddd.domain import GroupNotFoundError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import GroupUnitOfWorkImpl
from app.ddd.presentation.endpoint.group.router import router
from app.ddd.presentation.schema.group import GetGroupResponse


# #######################
def __usecase(session: Session = Depends(get_session)) -> GetGroupUseCase:
    return GetGroupUseCase(uow=GroupUnitOfWorkImpl(session))

################
@router.get(
    path="/groups/{groupId}",
    response_model=GetGroupResponse,
    responses={
        status.HTTP_404_NOT_FOUND: GroupNotFoundError(group_id="dammy").response(),
    },
)
def get_group(
    group_id: str = Path(..., alias="groupId"),
    usecase: GetGroupUseCase = Depends(__usecase),
) -> GetGroupResponse:
    """Groupを取得する."""
    input_dto: GetGroupInputDTO = GetGroupInputDTO(group_id=group_id)
    dto: GetGroupOutputDTO = usecase.execute(input_dto)
    return GetGroupResponse.model_validate(dto)


