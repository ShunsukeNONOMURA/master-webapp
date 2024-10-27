import os
from sqlmodel import Session, create_engine

db_engine = create_engine(
    url=os.getenv('SQLALCHEMY_DATABASE_URI'),
    echo=True,
)

def get_session():
    with Session(db_engine) as session:
        yield session
