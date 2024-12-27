# from fastapi import Depends, status
# from sqlmodel import Session

# from app.ddd.application.dto.user import CreateUserReportInputDTO, CreateUserReportOutputDTO
# from app.ddd.application.usecase.user import CreateUserReportUseCase
# from app.ddd.domain import UserDuplicationError
# from app.ddd.infrastructure.database.db import get_session
# from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
# from app.ddd.presentation.endpoint.user_report.router import router
# from app.ddd.presentation.schema.user import CreateUserReportRequest, CreateUsersResponse


# def __usecase(session: Session = Depends(get_session)) -> CreateUserReportUseCase:
#     return CreateUserReportUseCase(uow=UserUnitOfWorkImpl(session))


# @router.post(
#     path="/users/{userId}/user-reports",
#     response_model=CreateUsersResponse,
#     responses={
#         # status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
#     },
# )
# def create_users(
#     request: CreateUserReportRequest,
#     usecase: CreateUserReportUseCase = Depends(__usecase),
# ) -> CreateUsersResponse:
#     """ユーザを作成する."""
#     input_dto: CreateUserReportInputDTO = CreateUserReportInputDTO.model_validate(request)
#     dto: CreateUserReportOutputDTO = usecase.execute(input_dto)
#     return CreateUsersResponse.model_validate(dto)
