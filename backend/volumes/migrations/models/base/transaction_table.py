from datetime import datetime

from sqlmodel import Field

from .base_table import BaseTable


class TransactionTable(BaseTable):
    """
    トランザクションテーブル定義.

    Attributes
    ----------
    updated_at : datetime
        更新日時（UTC）

    """

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "onupdate": datetime.now,
            "comment": "更新日時（UTC）"
        },
    )
