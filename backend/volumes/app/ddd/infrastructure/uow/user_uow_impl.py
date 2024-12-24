from sqlmodel import Session

from app.ddd.application.uow import UserUnitOfWork
from app.ddd.infrastructure.repository import UserRepositoryImpl


class UserUnitOfWorkImpl(UserUnitOfWork):
    def __init__(self, session: Session) -> None:
        """UserUnitOfWork実装."""
        super().__init__(session, UserRepositoryImpl(session))
