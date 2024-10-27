from app.core.abstract.ddd import BaseUsecase
from app.ddd.application.schema.user import CreateUserParam, CreateUserDto
# from app.ddd.domain.user import 
from app.ddd.infra.repository.user_repository import UserRepository


from app.ddd.domain.user import User

from migrations.model.user_model import TUser

class CreateUserUseCase(BaseUsecase):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, param: CreateUserParam) -> CreateUserDto:
        user: User = User.model_validate(param)
        self.__user_repository.insert(user)
        return CreateUserDto(**user.to_dict())
    
    
