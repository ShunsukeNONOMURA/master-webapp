from abc import ABCMeta, abstractmethod

from sqlmodel import Session

from app.ddd.domain.model import (
    User,
    UserId,
)


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, db: Session) -> None:
        pass

    @abstractmethod
    def find_by_id(self, _id: UserId) -> User:
        raise NotImplementedError

    @abstractmethod
    def insert(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert_user_report(self, user: User) -> None:
        raise NotImplementedError


    @abstractmethod
    def update(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, _id: UserId) -> None:
        raise NotImplementedError

    @abstractmethod
    def query(self) -> list[User]:
        """
        TODO(nonomura): リポジトリでのメソッドかどうか要検討.

        多分クエリモデル文脈になるから分けたほうが良いかも
        """
        raise NotImplementedError
