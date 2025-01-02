
from sqlmodel import Field

from migrations.models.base import TransactionTable


class TGroup(TransactionTable, table=True):
    __tablename__ = "t_group"

    group_id: str = Field(primary_key=True, max_length=36, sa_column_kwargs={"comment": "PK　グループID"})
    group_name: str = Field(max_length=20, nullable = False, sa_column_kwargs={"comment": "グループ名"})

    group_responsible_user_id: str = Field(max_length=20, nullable = False,  foreign_key="t_user.user_id", sa_column_kwargs={"comment": "外部キー　グループ責任者ユーザid"})


    # 管理者、管理者

    # content: str = Field(
    #     sa_column=Column(
    #         Text,
    #         nullable = False,
    #         comment = "ユーザレポート内容",
    #     )
    # )
    # created_user_id: str = Field(
    #     max_length=20,
    #     foreign_key="t_user.user_id",
    #     sa_column_kwargs={"comment": "外部キー：ユーザID"}
    # )

    # user: Optional["TUser"] = Relationship(back_populates="user_reports") # error

