from types import TracebackType
from typing import TypeVar

from sqlmodel import Session

# サブクラス型を表す型パラメータ
BaseUnitOfWorkType = TypeVar("BaseUnitOfWorkType", bound="BaseUnitOfWork")

class BaseUnitOfWork:
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def __enter__(self: BaseUnitOfWorkType) -> BaseUnitOfWorkType:
        """__enter__の返り値がサブクラス型になるよう指定."""
        return self  # 型推論でサブクラス型 (T) が適用される

    def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_value: BaseException | None,
            traceback: TracebackType | None,
    ) -> None:
        """トランザクション管理."""
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
