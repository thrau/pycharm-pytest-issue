# testing-library/tests/test_example
from testing_library.fixtures import MyFixtureClass


def test_example(my_fixture):
    # here pycharm behaves as expected
    assert isinstance(my_fixture, MyFixtureClass)
