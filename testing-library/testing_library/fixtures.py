import pytest


class MyFixtureClass:
    pass


@pytest.fixture
def my_fixture():
    fixture = MyFixtureClass()

    yield fixture
