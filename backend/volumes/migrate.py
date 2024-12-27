from sqlalchemy import text
from sqlmodel import SQLModel

from app.ddd.domain import UserRoleEnum
from app.ddd.infrastructure.database.db import db_engine, db_name, get_session_context
from migrations.models.user_model import (
    MUserRole,
    TUser,
)


## extentionの有効化
def init_extention() -> None:
    # postgresの場合のextension有効化
    with get_session_context() as session:
        if db_name == "postgresql":
            session.execute(text("CREATE EXTENSION IF NOT EXISTS pgroonga"))
            session.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm"))
            print("pgroonga extension created successfully.")
            session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            print("pg_vector extension created successfully.")
        session.commit() # 手動コミット

# DDLの初期化
def init_ddl() -> None:
    SQLModel.metadata.drop_all(db_engine)
    SQLModel.metadata.create_all(bind=db_engine)

# レコードの初期化
def init_records() -> None:
    with get_session_context() as session:
        for user_role in UserRoleEnum:
            session.add(
                MUserRole(user_role_code=user_role.value, user_role_name=user_role.name)
            )
        user = TUser(
            user_id = "admin",
            user_name = "admin",
            user_password = "admin", # noqa: S106 (ダミーパスワードの手動設定に関するエラーを無視)
            user_role_code = "00",
        )
        session.add(user)
        user = TUser(
            user_id = "guest",
            user_name = "guest",
            user_password = "guest", # noqa: S106 (ダミーパスワードの手動設定に関するエラーを無視)
            user_role_code = "99",
        )
        session.add(user)
        session.commit()

# テーブル作成
if __name__ == "__main__":
    init_ddl()
    init_records()
