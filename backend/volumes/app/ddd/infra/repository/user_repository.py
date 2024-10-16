from abc import ABCMeta, abstractmethod
from datetime import datetime
from enum import Enum, unique

from pydantic import ConfigDict, Field, RootModel, SecretStr

from app.core import *
from app.ddd.infra.database.db import create_session
from migrations.model import *


@unique
class UserRoleEnum(Enum):
    Admin = "00"
    General = "10"
    Guest = "99"

class User(Entity):
    class UserId(ValueObject, RootModel):
        root: str
    class UserPassword(ValueObject, RootModel):
        root: SecretStr
    class UserName(ValueObject, RootModel):
        root: str
    class UserRoleCode(ValueObject, RootModel):
        root : UserRoleEnum = Field(description="ユーザロール")
    class UserRoleName(ValueObject, RootModel):
        root : str
    class UserCreationDatetime(ValueObject, RootModel):
        root: datetime
    class UserUpdateDatetime(ValueObject, RootModel):
        root: datetime

    user_id: UserId
    user_password: UserPassword
    user_name: UserName
    user_role_code: UserRoleCode
    user_role_name: UserRoleName
    user_creation_datetime: UserCreationDatetime
    user_update_datetime: UserUpdateDatetime

    def _id(self):
        return self.user_id

    model_config = ConfigDict(from_attributes=True)

class CreateUser(BaseSchema):
    user_id: str
    user_password: str
    user_name: str
    user_role_code: str
    # class UserId(ValueObject, RootModel):
    #     root: str
    # class UserPassword(ValueObject, RootModel):
    #     root: SecretStr
    # class UserName(ValueObject, RootModel):
    #     root: str
    # class UserRoleCode(ValueObject, RootModel):
    #     root : UserRoleEnum = Field(description="ユーザロール")




class IUserRepository(ABCMeta):
    # @abstractmethod
    # def __init__(self, db: Session) -> None:
    #     pass

    # @abstractmethod
    # def _fetch_by_id(self, user_id: StudentIdValueObject) -> StudentModel | None:
    #     pass

    # @abstractmethod
    # def _apply(self, model: StudentModel) -> StudentModel:
    #     pass

    @abstractmethod
    def find_by_id(self, user_id: User.UserId) -> User:
        pass

    @abstractmethod
    def insert(self, user: User):
        pass

    # @abstractmethod
    # def update(self, user: User) -> StudentModel:
    #     pass

    @abstractmethod
    def delete(self, user_id: User.UserId):
        pass

    # @abstractmethod
    # def refresh_to_entity(self, model: StudentModel) -> User:
    #     pass


from fastapi import status
from app.core.exception import DomainException

class UserNotFoundException(DomainException):
    def __init__(self):
        super().__init__(
            error_code='000',
            status_code=status.HTTP_404_NOT_FOUND,
            description="該当するユーザ情報が存在しません。",
        )


class UserRepository:
    def find_by_id(self, user_id: str):
        with create_session() as session:
            orm = session.query(VUser).filter(VUser.user_id == user_id).first()
            # orm = session.query(TUser).filter(TUser.user_id == user_id).first()
            model = User.model_validate(orm) if orm is not None else None
        if model is None:
            raise UserNotFoundException
        return model
    def query(self):
        with create_session() as session:
            users = session.query(VUser).all()
            # return users
            return [User.model_validate(orm) for orm in users]
    def insert(self, user: User):
        with create_session() as session:
            orm = TUser(**user.model_dump())
            session.add(orm)
            session.commit()
    def delete(self, user: User):
        with create_session() as session:
            orm = session.query(TUser).filter(TUser.user_id == user.user_id.root).first()
            session.delete(orm)
            session.commit()
