# my-app/tests/test_example
from testing_library.fixtures import MyFixtureClass


def test_example(my_fixture):
    # here pycharm cannot resolve the fixture or their type
    assert isinstance(my_fixture, MyFixtureClass)
