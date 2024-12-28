from abc import ABCMeta, abstractmethod

from app.ddd.domain.model import Token, User


class TokenFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self, user: User) -> Token:
        raise NotImplementedError
