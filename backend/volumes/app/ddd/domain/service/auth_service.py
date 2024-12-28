from abc import ABCMeta, abstractmethod


class AuthService(metaclass=ABCMeta):
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create_hashed_password(self, plain_password: str) -> str:
        raise NotImplementedError
