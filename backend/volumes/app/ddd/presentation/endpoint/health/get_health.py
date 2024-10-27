from fastapi import Path, Depends
from app.ddd.application.schema.health import GetHealthDto
from app.ddd.application.usecase.health import GetHealthUseCase
from app.ddd.presentation.endpoint.health.router import router
from app.ddd.presentation.schema.health import GetHealthResponse

def __user_dict():
    return {}

def __usecase() -> GetHealthUseCase:
    return GetHealthUseCase()

@router.get(
    path="/health",
    response_model=GetHealthResponse,
)
def get_health(
    usecase: GetHealthUseCase = Depends(__usecase),
    user_dict = Depends(__user_dict),
):
    dto: GetHealthDto = usecase.execute()
    response = GetHealthResponse.model_validate(dto)
    return response
