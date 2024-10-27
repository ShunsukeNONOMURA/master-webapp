from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import create_view

from sqlalchemy.orm import registry

from sqlmodel import SQLModel, Field, Column, text, SmallInteger, Text

from app.core.mixin import SQLModelGenerateMixin

table_args = {}
# table_args = {'extend_existing': True}
# table_args = {'schema': 'app'}

# Base = declarative_base()


class TUser(SQLModel, SQLModelGenerateMixin, table=True):
    __table_args__ = table_args
    __tablename__ = "t_user"

    user_id: str = Field(primary_key=True, max_length=20, sa_column_kwargs={"comment": "ユーザID"})
    user_name: str = Field(max_length=20, nullable=False, sa_column_kwargs={"comment": "ユーザ名"})
    user_password: str = Field(max_length=20, nullable=False, sa_column_kwargs={"comment": "ユーザパスワード"})
    user_creation_datetime: datetime = Field(nullable=False, default_factory=datetime.utcnow, sa_column_kwargs={"comment": "ユーザ作成日"})
    user_update_datetime: datetime = Field(nullable=False, default_factory=datetime.utcnow, sa_column_kwargs={"comment": "ユーザ更新日"})
    user_role_code: str = Field(max_length=20, nullable=False, foreign_key="m_user_role.user_role_code", sa_column_kwargs={"comment": "ユーザロールコード"})


class MUserRole(SQLModel, table=True):
    __table_args__ = table_args
    __tablename__ = "m_user_role"

    user_role_code: str = Field(primary_key=True, max_length=2, sa_column_kwargs={"comment": "ユーザロールコード"})
    user_role_name: str = Field(nullable=False, max_length=30, sa_column_kwargs={"comment": "ユーザロール名"})



# # Userテーブルの定義
# class TUser(Base):
#     __table_args__ = table_args
#     __tablename__ = "t_user"
#     user_id = Column(String(20), primary_key = True, comment="ユーザID")
#     user_name = Column(String(20), nullable=False)
#     user_password = Column(String(20), nullable=False)
#     user_creation_datetime = Column(DATETIME, default=datetime.now, nullable=False)
#     user_update_datetime = Column(DATETIME, default=datetime.now, nullable=False)
#     user_role_code = Column(String(2), ForeignKey("m_user_role.user_role_code"), nullable=False)

# # Userロールの定義
# class MUserRole(Base):
#     __table_args__ = table_args
#     __tablename__ = "m_user_role"
#     user_role_code = Column(String(2), primary_key = True)
#     user_role_name = Column(String(20), nullable=False)
#     user = relationship("TUser")



# class VUser(SQLModel, table=True):
# # class VUser(Base):
#     __table__ = create_view(
#         "v_user",
#         select(
#             TUser.user_id,
#             TUser.user_name,
#             TUser.user_password,
#             TUser.user_creation_datetime,
#             TUser.user_update_datetime,
#             TUser.user_role_code,
#             MUserRole.user_role_name,
#         ).select_from(TUser.__table__.outerjoin(MUserRole, MUserRole.user_role_code == TUser.user_role_code)),
#         metadata=SQLModel.metadata,
#         cascade_on_drop=False,
#         # replace = True
#     )

# mapper_registry = registry()
# mapper_registry.map_imperatively(VUser.__table__)


# class TTmp(SQLModel, table=True):
#     __table_args__ = table_args
#     __tablename__ = "t_tmp"

#     id: str = Field(primary_key=True, max_length=50, sa_column_kwargs={"comment": "tmp id"})
