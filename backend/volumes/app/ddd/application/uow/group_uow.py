from sqlmodel import Session

from app.core.base import BaseUnitOfWork
from app.ddd.domain.repository import GroupRepository


class GroupUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session, group_repository: GroupRepository) -> None:
        """Group用UnitOfWork."""
        super().__init__(session)
        self.group_repository = group_repository
