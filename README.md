# pycharm pytest plugin reproducer

pycharm does not resolve pytest plugins correctly when they are located in dependent projects when they are attached or installed as editable

* run `make install` in `testing-library`
* run `make install` in `my-app`
* open `my-ap` in pycharm as new project
* attach `testing-library` to the pycharm project

navigate to `test_example.py` and observe that pycharm cannot navigate to `my_fixture` or resolve its type.


The two apps were created with cookiecutter https://github.com/localstack/cookiecutter/tree/main/python-application

