import pytest

from migrate import init_ddl, init_records
@pytest.fixture(scope="function")
def db():
    init_ddl()
    init_records()
    yield
