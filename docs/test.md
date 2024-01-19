# Testing
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