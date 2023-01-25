# pycharm pytest plugin reproducer

pycharm does not resolve pytest plugins correctly when they are located in dependent projects when they are attached or installed as editable

* run `make install` in `testing-library`
* run `make install` in `my-app`
* open `my-ap` in pycharm as new project
* attach `testing-library` to the pycharm project

navigate to `test_example.py` and observe that pycharm cannot navigate to `my_fixture` or resolve its type.


The two apps were created with cookiecutter https://github.com/localstack/cookiecutter/tree/main/python-application

## Screenshot

the left side shows files in my-app, the right side shows files in testing-library.
note that pycharm cannot resolve the pytest fixture in `my-app`.

![Screenshot at 2023-01-25 23-26-05](https://user-images.githubusercontent.com/3996682/214706213-ed4d49d1-42aa-4e05-9f82-607daae2559c.png)
