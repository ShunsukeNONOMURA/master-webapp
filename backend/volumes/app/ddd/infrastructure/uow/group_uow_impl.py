from sqlmodel import Session

from app.ddd.application.uow import GroupUnitOfWork
from app.ddd.infrastructure.repository import GroupRepositoryImpl


class GroupUnitOfWorkImpl(GroupUnitOfWork):
    def __init__(self, session: Session) -> None:
        """GroupUnitOfWork実装."""
        super().__init__(session, GroupRepositoryImpl(session))
