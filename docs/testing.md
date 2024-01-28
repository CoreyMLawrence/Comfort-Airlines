# Testing
Testing is a crucial part of building software systems. Tests provide the developers assurance that the system
meets client expectations and provides the client assurance that the system is robust, suitable for real-world
application. As a part of our test-driven development lifecycle, every component of the software system should 
be rigorously tested.

# Types of Testing
The `tests` folder has been divided into three major categories: unit, integration, and system
tests. Although [there are many types of tests](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing),
we will only leverage component-oriented tests.

## Unit Tests
Unit tests test individual components of a system and should be written immediately after finishing the component.
Unit tests should cover all possible combinations of values categories of input to check all possible behaviors.
Unit tests should contain erroneous input to check whether the component handles errors correctly. If a component
depends on another component (e.g a data source like a database), the dependencies must be 
[mocked](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/unit-testing/mocking/).

# Integration Tests
Integration tests test the two dependent components, such as an application's ability to perform CRUD operations
on a database. System tests test the entire system, front to back. There will only be one set of integration tests
for this project: the connection between the Python application and the MariaDB database. The tests should
ensure that the application can
1. Connect to the MariaDB database securely
2. Perform CRUD operations

# System Tests (E2E)
To ensure the developed product meets project requirements, the product must undergo system tests.
System tests test the product from beginning to end as a collection of integrated components. For this
reason, system tests are often also called end-to-end tests; though, system tests can also test subsystems 
(sets of related components).

System testing is a level of testing that validates the complete and fully integrated software product. The purpose of a system test is to evaluate the end-to-end system specifications

# Implementing Tests with Pytest
For testing, we will use the [pytest](https://docs.pytest.org/en/7.4.x/) testing framework. If you do
not have pytest installed, you can install it by running `pip3 install -r requirements.txt`.
To write tests with pytest, just create a new python file in the `tests` directory, import your code
with the  *[import](https://realpython.com/python-import/#basic-python-import)* keyword, and write a 
function to test it. The name of the test file and test method should start with `test_`.
You can write more than one test method per file and are encouraged to group similar tests
in the same python file. To run your tests, just run `python3 -m pytest`. Assuming you followed 
the naming conventions above correctly, pytest will automatically discover and run your tests.

```py
# mathematics.py
# > some pretend code you want to test
def add(x: int, y: int) -> int:
    return x + y
```

```py
# test_mathematics.py
# > an example test file
import mathematics

def test_add() -> None:
    assert mathematics.add(2,3) == 5
```