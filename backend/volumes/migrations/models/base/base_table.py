from datetime import datetime

from sqlmodel import Field, SQLModel


class BaseTable(SQLModel):
    """
    必須プロパティを持つベーステーブル定義.

    Attributes
    ----------
    created_at : datetime
        作成日時（UTC）

    """

    # OracleではAuto Incrementされないのでこの記述は使えない
    # id: int = Field(
    #     primary_key=True,
    #     sa_column_kwargs={"comment": "ORM対応用途のAIなPK"},
    # )

    # 各具象クラスで Column object 'id' already assigned to Table となり、テーブルごとの定義にならないのでこの方法も使えない
    # id: int = Field(
    #     sa_column=Column(
    #         Integer,
    #         Identity(always=True),
    #         primary_key=True,
    #         comment='ORM対応用途のAIなPK',
    #     )
    # )

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"comment": "作成日時（UTC）"},
    )
