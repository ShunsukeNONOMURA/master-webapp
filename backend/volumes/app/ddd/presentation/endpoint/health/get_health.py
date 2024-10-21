from app.ddd.presentation.endpoint.health.router import router

from app.ddd.presentation.schema.health import (
    GetHealthRequest,
    GetHealthResponse
)

from app.ddd.application.schema.health import (
    GetHealthDto
)

from app.ddd.application.usecase.health import (
    GetHealth
)

@router.get(
    path="/health",
    response_model=GetHealthResponse,
)
def get_health():
    dto: GetHealthDto = GetHealth().execute()
    return dto
