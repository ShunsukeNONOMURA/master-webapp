from app.ddd.domain.user import User, UserId
from migrations.model import TUser

from sqlmodel import Session, select

# class CreateUser(BaseSchema):
#     user_id: str
#     user_password: str
#     user_name: str
#     user_role_code: str



from fastapi import status

from app.core.exception import DomainException


class UserNotFoundException(DomainException):
    def __init__(self):
        super().__init__(
            error_code="999",
            status_code=status.HTTP_404_NOT_FOUND,
            description="該当するユーザ情報が存在しません。",
        )


class UserRepository:
    def __init__(self, session: Session):
        self.__session: Session = session
    
    def _fetch_by_id(self, user_id: UserId) -> TUser | None:
        statement = select(TUser).where(TUser.user_id == user_id.root)
        t_user = self.__session.exec(statement).first()
        return t_user

    def _apply(self, model: TUser) -> TUser:
        self.__session.add(model)
        self.__session.commit()
        return model


    def find_by_id(self, user_id: UserId) -> User:
        t_user = self._fetch_by_id(user_id)
        if t_user is None:
            raise UserNotFoundException
        return User.from_model(t_user)
    
    def query(self):
        users = self.__session.query(TUser).all()
        return [User.model_validate(orm) for orm in users]

    def insert(self, user: User) -> User:
        t_user: TUser = TUser.generate_by(user)
        print(t_user)
        # t_user: TUser = TUser.model_validate(user) # validation error
        # self._apply(t_user)
        return user

    def delete(self, user_id: UserId) -> TUser:
        t_user = self._fetch_by_id(user_id)
        if t_user is None:
            raise UserNotFoundException
        print(t_user)
        self.__session.delete(t_user)
        self.__session.commit()
        return user_id
