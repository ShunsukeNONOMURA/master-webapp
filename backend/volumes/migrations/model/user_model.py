from datetime import datetime

from sqlalchemy import DATETIME, Column, ForeignKey, String, select
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import create_view

table_args = {}
# table_args = {'schema': 'app'}

Base = declarative_base()

# Userテーブルの定義
class TUser(Base):
    __table_args__ = table_args
    __tablename__ = "t_user"
    user_id = Column(String(20), primary_key = True, comment="ユーザID")
    user_name = Column(String(20), nullable=False)
    user_password = Column(String(20), nullable=False)
    user_creation_datetime = Column(DATETIME, default=datetime.now, nullable=False)
    user_update_datetime = Column(DATETIME, default=datetime.now, nullable=False)
    user_role_code = Column(String(2), ForeignKey("m_user_role.user_role_code"), nullable=False)

# Userロールの定義
class MUserRole(Base):
    __table_args__ = table_args
    __tablename__ = "m_user_role"
    user_role_code = Column(String(2), primary_key = True)
    user_role_name = Column(String(20), nullable=False)
    user = relationship("TUser")

class VUser(Base):
    __table__ = create_view(
        "v_user",
        select(
            TUser.user_id,
            TUser.user_name,
            TUser.user_password,
            TUser.user_creation_datetime,
            TUser.user_update_datetime,
            TUser.user_role_code,
            MUserRole.user_role_name,
        ).select_from(TUser.__table__.outerjoin(MUserRole, MUserRole.user_role_code == TUser.user_role_code)),
        metadata = Base.metadata,
        cascade_on_drop=False,
        # replace = True
    )
