from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.presentation.endpoint.users.router import router


@router.delete(
    path="/users/{user_id}",
)
def delete_user(user_id: str):
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    user = user_repository.delete(user)
    return user
