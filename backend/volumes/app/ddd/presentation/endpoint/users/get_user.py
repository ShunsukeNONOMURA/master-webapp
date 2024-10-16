from app.ddd.infra.repository.user_repository import UserRepository
from app.ddd.presentation.endpoint.users.router import router


@router.get(
    path="/users/{user_id}",
)
def get_user(user_id: str):
    # db: Session = Depends(get_db)
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    return user
