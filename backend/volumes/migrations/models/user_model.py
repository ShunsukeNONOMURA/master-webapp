from sqlmodel import Field

from migrations.models.base import MasterTable, TransactionTable


class TUser(TransactionTable, table=True):
    # __table_args__ = table_args
    __tablename__ = "t_user"

    user_id: str = Field(primary_key=True, max_length=20, sa_column_kwargs={"comment": "ユーザID"})
    user_name: str = Field(max_length=20, nullable=False, sa_column_kwargs={"comment": "ユーザ名"})
    user_password: str = Field(max_length=20, nullable=False, sa_column_kwargs={"comment": "ユーザパスワード"})
    user_role_code: str = Field(max_length=20, nullable=False, foreign_key="m_user_role.user_role_code", sa_column_kwargs={"comment": "ユーザロールコード"})

class MUserRole(MasterTable, table=True):
    # __table_args__ = table_args
    __tablename__ = "m_user_role"

    user_role_code: str = Field(primary_key=True, max_length=2, sa_column_kwargs={"comment": "ユーザロールコード"})
    user_role_name: str = Field(nullable=False, max_length=30, sa_column_kwargs={"comment": "ユーザロール名"})
