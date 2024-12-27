from typing import Optional

from pydantic import SecretStr
from sqlalchemy import Column
from sqlmodel import Field, Relationship, String

from migrations.models.base import MasterTable, TransactionTable


class TUserReport(TransactionTable, table=True):
    __tablename__ = "t_user_report"

    user_report_id: str = Field(primary_key=True, max_length=36, sa_column_kwargs={"comment": "ユーザレポートID"})
    title: str = Field(max_length=20, sa_column_kwargs={"comment": "ユーザレポートタイトル"})
    content: str = Field(max_length=20, sa_column_kwargs={"comment": "ユーザレポート内容"})
    created_user_id: str = Field(
        max_length=20,
        foreign_key="t_user.user_id",
        sa_column_kwargs={"comment": "外部キー：ユーザID"}
    )

    user: Optional["TUser"] = Relationship(back_populates="user_reports") # error

class TUser(TransactionTable, table=True):
    # __table_args__ = table_args
    __tablename__ = "t_user"

    user_id: str = Field(primary_key=True, max_length=20, sa_column_kwargs={"comment": "ユーザID"})
    user_name: str = Field(max_length=20, nullable=False, sa_column_kwargs={"comment": "ユーザ名"})
    user_password: SecretStr = Field(
        sa_column=Column(
            String(20),
            nullable = False,
            comment = "ユーザパスワード",
        )
    )
    # hashed_password: SecretStr = Field(
    #     sa_column=Column(
    #         String(20),
    #         nullable = False,
    #         comment = "ユーザhashパスワード",
    #     )
    # )
    user_role_code: str = Field(max_length=20, nullable=False, foreign_key="m_user_role.user_role_code", sa_column_kwargs={"comment": "ユーザロールコード"})

    # __mapper_args__ = {
    #     'version_id_col': updated_at
    # }

    user_reports: list[TUserReport] = Relationship(back_populates="user", cascade_delete=True)


class MUserRole(MasterTable, table=True):
    # __table_args__ = table_args
    __tablename__ = "m_user_role"

    user_role_code: str = Field(primary_key=True, max_length=2, sa_column_kwargs={"comment": "ユーザロールコード"})
    user_role_name: str = Field(nullable=False, max_length=30, sa_column_kwargs={"comment": "ユーザロール名"})
