from contextlib import contextmanager
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import DATETIME, Column, ForeignKey, String, create_engine, select


SQLALCHEMY_DATABASE_URI = "sqlite:///./dev.sqlite3"
# SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
    echo=True,
)
# DB接続用のセッションクラス インスタンスが作成されると接続する
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

# DB接続のセッションを各エンドポイントの関数に渡す
@contextmanager
def create_session():
    session = SessionLocal()  # def __enter__
    try:
        yield session  # with asでsessionを渡す
        session.commit()  # 何も起こらなければcommit()
    except:
        print("rollback transaction")
        session.rollback()  # errorが起こればrollback()
        raise
    finally:
        print("closing connection")
        session.close()  # どちらにせよ最終的にはclose()



from sqlmodel import Session, create_engine


def get_db_url() -> str:
    dialect = "postgresql"
    driver = "psycopg2"
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = "5432"
    database = "teckteckt_ddd_python"
    return f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}"



__db_engine = create_engine(
    # url=get_db_url(),
    url=SQLALCHEMY_DATABASE_URI,
    echo=True,
)


def get_db() -> Session:
    with Session(__db_engine) as session:
        yield session
