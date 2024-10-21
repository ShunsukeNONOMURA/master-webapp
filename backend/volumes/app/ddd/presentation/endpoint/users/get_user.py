from app.ddd.presentation.endpoint.users.router import router

from app.ddd.presentation.schema.users import (
    GetUsersUserResponse
)

from app.ddd.application.schema.user import (
    GetUserDto,
)

from app.ddd.application.usecase.user import (
    GetUsersUseCase,
    GetUserUseCase,
)

@router.get(
    path="/users",
    # response_model=GetUsersResponse,
)
def get_users(
):
    # db: Session = Depends(get_db)
    usecase = GetUsersUseCase()
    dto : GetUserDto = usecase.execute()
    return dto

@router.get(
    path="/users/{user_id}",
    response_model=GetUsersUserResponse,
)
def get_user(
    user_id: str,
):
    # db: Session = Depends(get_db)
    usecase = GetUserUseCase()
    dto : GetUserDto = usecase.execute(user_id)
    return dto
