from enum import Enum, unique
from pydantic import ConfigDict, Field, RootModel, SecretStr

from app.core.abstract.ddd import Entity, ValueObject

from migrations.model import TUser

from datetime import datetime

@unique
class UserRoleEnum(Enum):
    Admin = "00"
    General = "10"
    Guest = "99"

# class User2(Entity):
#     class UserId(ValueObject, RootModel):
#         root: str
#     class UserPassword(ValueObject, RootModel):
#         root: SecretStr
#     class UserName(ValueObject, RootModel):
#         root: str
#     class UserRoleCode(ValueObject, RootModel):
#         root : UserRoleEnum = Field(description="ユーザロール")
#     class UserRoleName(ValueObject, RootModel):
#         root : str
#     class UserCreationDatetime(ValueObject, RootModel):
#         root: datetime
#     class UserUpdateDatetime(ValueObject, RootModel):
#         root: datetime

#     user_id: UserId
#     user_password: UserPassword
#     user_name: UserName
#     user_role_code: UserRoleCode
#     user_role_name: UserRoleName
#     user_creation_datetime: UserCreationDatetime
#     user_update_datetime: UserUpdateDatetime

#     def _id(self):
#         return self.user_id

#     model_config = ConfigDict(from_attributes=True)

#     @classmethod
#     def from_model(cls, model: TUser) -> "User":
#         return User(
#             **model.dict()
#         )

class UserId(ValueObject):
    root: str

class User(Entity):
    user_id: str
    user_password: SecretStr
    user_name: str
    user_role_code: str
    # user_role_name: str
    user_creation_datetime: datetime | None = None
    user_update_datetime: datetime | None = None

    def _id(self):
        return self.user_id

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_model(cls, model: TUser) -> "User":
        return User(
            **model.dict()
        )
    

from sqlmodel import Session
from abc import ABCMeta, abstractmethod

class IUserRepository(ABCMeta):
    @abstractmethod
    def __init__(self, session: Session) -> None:
        pass

    # @abstractmethod
    # def _fetch_by_id(self, user_id: UserId) -> User | None:
    #     pass

    # @abstractmethod
    # def _apply(self, model: StudentModel) -> StudentModel:
    #     pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def insert(self, user: User):
        pass

    # @abstractmethod
    # def update(self, user: User) -> StudentModel:
    #     pass

    @abstractmethod
    def delete(self, user_id: UserId):
        pass

    # @abstractmethod
    # def refresh_to_entity(self, model: StudentModel) -> User:
    #     pass