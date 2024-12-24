import pytest

from migrate import init_ddl, init_records
@pytest.fixture(scope="function")
def db():
    print('on fixture')
    init_ddl()
    init_records()
    yield
