# Pytest crash course. Summary of the following tutorial: https://youtu.be/cHYq1MRoyI0
#
# Pytest will automatically detect and run your tests when you run "python3 -m pytest".
# HOWEVER, it will only detect test files whose name starts with "test_" in the "tests"
# folder or any of its subfolders and will only run tests who name starts with "test_". 
# So just prefix everything with "test_", got it?

# Start by importing pytest
import pytest

# Then import whatever you're testing. If you're importing the entire file (module)
# then you can just write "import src.FILENAME", but if you're importing something specific
# then you havve to write "from src.FILENAME import X, Y, Z".

# To write a test, define a method whose name starts with "test_" and returns `None`.
# Test your code with `assert` statements: https://www.w3schools.com/python/ref_keyword_assert.asp
def test_add() -> None:
    assert 10 == 10

# You test that a function throws an error by prefixing the block that should throw with `pytest.raises(ERROR)`
def test_div() -> None:
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0 == 0

# You can test a method with multiple sets of data by parametrizing it. Just define the variables in the function parameter list,
# mark the test as parametrized, and then pass it variables names in a comma-separated list and the values in a list of tuples
@pytest.mark.parametrize("x, y", [(10,5), (3,2), (-10,3)])
def test_parameterized(x: int, y: int) -> None:
    assert ((x + y) << 1 >> 1) == x + y
    
# Now, run your tests with "python3 -m pytest". 
# If it's not installed, run "pip3 install -r requirements.txt"
