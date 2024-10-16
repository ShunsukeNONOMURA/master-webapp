from app.ddd.presentation.endpoint.health.router import router


@router.get(
    path="/health",
    # tags=["health"]
)
def get_health():
    return {"msg": "ok"}
