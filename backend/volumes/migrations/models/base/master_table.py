from datetime import datetime

from sqlmodel import Field

from .base_table import BaseTable


class MasterTable(BaseTable):
    """
    マスタテーブル定義.

    Attributes
    ----------
    updated_at : datetime
        更新日時（UTC）

    """

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "onupdate": datetime.utcnow,
            "comment": "更新日時（UTC）"
        },
    )

    # @root_validator(pre=True)
    # def set_timestamps(self, values):
    #     """作成日情報が存在しない場合は作成日と更新日を同じ現在時刻で新規作成する。."""
    #     if values.get("created_at") is None:
    #         now = datetime.utcnow()
    #         values["created_at"] = now
    #         values["updated_at"] = now
    #     return values
