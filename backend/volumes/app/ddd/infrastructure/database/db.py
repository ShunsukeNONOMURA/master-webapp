import os
from collections.abc import Generator
from contextlib import contextmanager

from sqlmodel import Session, create_engine

db_name = os.environ["SQLALCHEMY_DATABASE"]

__db_urls = {
    "sqlite": os.environ["SQLALCHEMY_DATABASE_SQLITE_URI"],
    "postgresql": os.environ["SQLALCHEMY_DATABASE_POSTGRES_URI"],
}

url = __db_urls[db_name]

db_engine = create_engine(
    url=url,
    echo=False, # SQL見る場合に有効化する
)

# 手動実行用途で分離
@contextmanager
def get_session_context() -> Generator[Session]:
    with Session(db_engine) as session:
        yield session

def get_session() -> Generator[Session]:
    with get_session_context() as session:
        yield session
