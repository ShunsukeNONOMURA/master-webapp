from app.core.abstract.ddd import BaseUsecase
from app.ddd.application.schema.user import GetUserParam, GetUserDto
from app.ddd.infra.repository.user_repository import (
    UserRepository, 
    UserId,
)
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

class GetUsersUseCase(BaseUsecase):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self) -> GetUserDto:
        users = self.__user_repository.query()
        return users
        # return GetUserDto(**users.to_dict())

class GetUserUseCase(BaseUsecase):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, param: GetUserParam) -> GetUserDto:
        user_id = UserId(root=param.user_id)
        user = self.__user_repository.find_by_id(user_id)
        # print(user.model_dump())
        return GetUserDto(**user.model_dump())
