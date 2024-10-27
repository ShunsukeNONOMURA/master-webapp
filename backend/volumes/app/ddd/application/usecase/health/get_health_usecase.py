from app.core.abstract.ddd import BaseUsecase
from app.ddd.application.schema.health import GetHealthDto


class GetHealthUseCase(BaseUsecase):
    def __init__(self):
        pass

    def execute(self) -> GetHealthDto:
        return GetHealthDto(msg="ok")
