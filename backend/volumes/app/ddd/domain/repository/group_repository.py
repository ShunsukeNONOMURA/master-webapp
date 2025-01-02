from abc import ABCMeta, abstractmethod

from sqlmodel import Session

from app.ddd.domain.model import (
    Group,
    GroupId,
)


class GroupRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, db: Session) -> None:
        pass

    @abstractmethod
    def find_by_id(self, _id: GroupId) -> Group:
        raise NotImplementedError

    @abstractmethod
    def insert(self, user: Group) -> None:
        raise NotImplementedError

    # @abstractmethod
    # def insert_user_report(self, user: Group) -> None:
    #     raise NotImplementedError


    # @abstractmethod
    # def update(self, user: Group) -> None:
    #     raise NotImplementedError

    @abstractmethod
    def delete(self, _id: GroupId) -> None:
        raise NotImplementedError

    @abstractmethod
    def query(self) -> list[Group]:
        """
        TODO(nonomura): リポジトリでのメソッドかどうか要検討.

        多分クエリモデル文脈になるから分けたほうが良いかも
        """
        raise NotImplementedError
