
from fastapi import Depends, status
from sqlmodel import Session

from app.ddd.application.dto.group import CreateGroupInputDTO, CreateGroupOutputDTO
from app.ddd.application.usecase.group import CreateGroupUseCase
from app.ddd.domain import GroupDuplicationError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import GroupUnitOfWorkImpl
from app.ddd.presentation.endpoint.group.router import router
from app.ddd.presentation.schema.group import CreateGroupRequest, CreateGroupResponse


def __usecase(session: Session = Depends(get_session)) -> CreateGroupUseCase:
    return CreateGroupUseCase(uow=GroupUnitOfWorkImpl(session))


@router.post(
    path="/groups",
    # response_model=CreateGroupResponse,
    responses={
        status.HTTP_409_CONFLICT: GroupDuplicationError(group_id="dammy").response(),
    },
)
def create_group(
    request: CreateGroupRequest,
    # jwt_data: dict[str, Any] = Depends(jwt_data_depends),
    usecase: CreateGroupUseCase = Depends(__usecase),
) -> CreateGroupResponse:
    # return {}
    """Groupを作成する."""
    input_dto: CreateGroupInputDTO = CreateGroupInputDTO.model_validate(
        {
            "group_responsible_user_id": "admin", #jwt_data['sub'],
            **request.model_dump(exclude_unset=True)
        }
    )
    dto: CreateGroupOutputDTO = usecase.execute(input_dto)
    return CreateGroupResponse.model_validate(dto)
