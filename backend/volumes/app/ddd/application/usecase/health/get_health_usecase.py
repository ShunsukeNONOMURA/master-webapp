from app.core.base import BaseInputDTO, BaseUsecase
from app.ddd.application.schema.health import GetHealthOutputDTO


class GetHealthUseCase(BaseUsecase):
    def __init__(self) -> None:
        pass

    def execute(self, _: BaseInputDTO) -> GetHealthOutputDTO:
        return GetHealthOutputDTO(msg="ok")
