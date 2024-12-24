
from app.ddd.presentation.endpoint.health.router import router
from app.ddd.presentation.schema.health import GetHealthResponse


@router.get(
    path="/health",
    response_model=GetHealthResponse,
)
def get_health() -> GetHealthResponse:
    """ヘルスの取得."""
    return GetHealthResponse.model_validate({"status": "green"})
