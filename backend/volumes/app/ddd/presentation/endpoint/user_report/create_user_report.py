from fastapi import Depends, Path, status
from sqlmodel import Session

from app.ddd.application.dto.user import (
    CreateUserReportInputDTO,
    CreateUserReportOutputDTO,
)
from app.ddd.application.usecase.user import CreateUserReportUseCase
from app.ddd.domain import UserNotFoundError
from app.ddd.infrastructure.database.db import get_session
from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
from app.ddd.presentation.endpoint.user_report.router import router
from app.ddd.presentation.schema.user_report import (
    CreateUserReportRequest,
    CreateUserReportResponse,
)


def __usecase(session: Session = Depends(get_session)) -> CreateUserReportUseCase:
    return CreateUserReportUseCase(uow=UserUnitOfWorkImpl(session))


@router.post(
    path="/users/{userId}/user-reports",
    response_model=CreateUserReportResponse,
    responses={
        status.HTTP_404_NOT_FOUND: UserNotFoundError(user_id="dammy").response(),
        # status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
    },
)
def create_user_report(
    request: CreateUserReportRequest,
    user_id: str = Path(..., alias="userId"),
    usecase: CreateUserReportUseCase = Depends(__usecase),
) -> CreateUserReportResponse:
    """ユーザレポートを作成する."""
    input_dto: CreateUserReportInputDTO = CreateUserReportInputDTO.model_validate({"user_id": user_id, **request.model_dump(exclude_unset=True)})
    dto: CreateUserReportOutputDTO = usecase.execute(input_dto)
    return CreateUserReportResponse.model_validate(dto)
