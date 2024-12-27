from app.ddd.application.dto.user import (
    CreateUserReportInputDTO,
    CreateUserReportOutputDTO,
)
from app.ddd.application.usecase.user.base_user_usecase import BaseUserUseCase
from app.ddd.domain.model import UserId


class CreateUserReportUseCase(BaseUserUseCase[CreateUserReportInputDTO, CreateUserReportOutputDTO]):
    def execute(self, input_dto: CreateUserReportInputDTO) -> CreateUserReportOutputDTO:
        user_id = UserId(root=input_dto.user_id)
        user = self._uow.user_repository.find_by_id(user_id)
        user_report = user.add_report(**input_dto.model_dump())

        print(user_report)

        # user_report: User = User.model_validate(input_dto)
        with self._uow:
            self._uow.user_repository.insert_user_report(user)
        return CreateUserReportOutputDTO(
            user_report_id = user_report.user_report_id
        )
