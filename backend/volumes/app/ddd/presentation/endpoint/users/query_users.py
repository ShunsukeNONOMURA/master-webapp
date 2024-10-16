from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.presentation.endpoint.users.router import router


@router.get(
    path="/query/users",
)
def query_user(q: str = ""):
    user_repository = UserRepository()
    users = user_repository.query()
    return users
    return {"q": q}
