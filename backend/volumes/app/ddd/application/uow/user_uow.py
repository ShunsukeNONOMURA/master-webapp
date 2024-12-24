from sqlmodel import Session

from app.core.base import BaseUnitOfWork
from app.ddd.domain.repository import UserRepository


class UserUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session, user_repository: UserRepository) -> None:
        """User用UnitOfWork."""
        super().__init__(session)
        self.user_repository = user_repository
