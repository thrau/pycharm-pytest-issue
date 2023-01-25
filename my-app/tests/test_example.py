from testing_library.fixtures import MyFixtureClass


def test_example(my_fixture):
    # it works, but pycharm does not resolve the fixture type correctly
    # (can't navigate to the definition, and don't get type hints)
    assert isinstance(my_fixture, MyFixtureClass)
