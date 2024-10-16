from app.ddd.infra.repository.user_repository import CreateUser, UserRepository
from app.ddd.presentation.endpoint.users.router import router


@router.post(
    path="/users",
)
def create_user(user: CreateUser):
    print(user)
    # user = User.model_validate(
    #     user
    # )
    user_repository = UserRepository()
    user = user_repository.insert(user)
    return user
