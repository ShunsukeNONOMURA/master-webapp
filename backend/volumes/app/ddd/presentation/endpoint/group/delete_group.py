from fastapi import Depends, Path
from sqlmodel import Session

from app.ddd.application.dto.group import DeleteGroupInputDTO, DeleteGroupOutputDTO
from app.ddd.application.usecase.group import DeleteGroupUseCase
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import GroupUnitOfWorkImpl
from app.ddd.presentation.endpoint.group.router import router
from app.ddd.presentation.schema.group import DeleteGroupResponse


def __usecase(session: Session = Depends(get_session)) -> DeleteGroupUseCase:
    return DeleteGroupUseCase(uow=GroupUnitOfWorkImpl(session))

@router.delete(
    path="/groups/{groupId}",
    response_model=DeleteGroupResponse,
    responses={
        # TODO(nonomura): Error 1:n ErrorResponse.errors
        # status.HTTP_404_NOT_FOUND: GroupNotFoundError(group_id='dammy').response(),
        # status.HTTP_404_NOT_FOUND: {
        #     "content": {
        #         "application/json": {
        #             "example": {
        #                 "detail": [
        #                     GroupNotFoundError(group_id="dammy").camel_detail(),
        #                 ]
        #             }
        #         }
        #     },
        # }
    },

)
def delete_group(
    group_id: str = Path(..., alias="groupId"),
    usecase: DeleteGroupUseCase = Depends(__usecase),
) -> DeleteGroupResponse:
    """Groupを削除する."""
    input_dto: DeleteGroupInputDTO = DeleteGroupInputDTO(group_id=group_id)
    dto: DeleteGroupOutputDTO = usecase.execute(input_dto)
    return DeleteGroupResponse.model_validate(dto)
