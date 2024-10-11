"""このモジュールの説明
"""
from contextlib import contextmanager

from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import DATETIME, Column, ForeignKey, String, create_engine, select

from migrations.db import *




# RDBの初期化
def init_db(drop_all: bool=True) -> None:
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)

    with create_session() as session:
        user_role = MUserRole(user_role_code="00", user_role_name="admin")
        session.add(user_role)
        user_role = MUserRole(user_role_code="99", user_role_name="guest")
        session.add(user_role)
        user = TUser(
            user_id = "admin",
            user_name = "admin",
            user_password = "admin",
            user_role_code = "00",
        )
        session.add(user)
        user = TUser(
            user_id = "guest",
            user_name = "guest",
            user_password = "guest",
            user_role_code = "99",
        )
        session.add(user)
        session.commit()

# テーブル作成
if __name__ == "__main__":
    init_db()
