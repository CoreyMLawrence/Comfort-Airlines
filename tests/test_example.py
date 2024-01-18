# Pytest Crash Course
#
# Pytest will automatically detect and run your tests when you run "python3 -m pytest".
# HOWEVER, it will only detect test files whose name starts with "test_" in the "tests"
# folder or any of its subfolders and will only run tests who name starts with "test_". 
# So just prefix everything with "test_", got it?

# Start by importing whatever you're testing. If you're importing the entire file (module)
# then you can just write "import src.FILENAME", but if you're importing something specific
# then you havve to write "from src.FILENAME import FOO, BAR, BAZ".
import src.main

# To write a test, define a method whose name starts with "test_" and returns `None`.
# Test your code with `assert` statements: https://www.w3schools.com/python/ref_keyword_assert.asp
def test_add() -> None:
    assert 10 == 10
    
# Now, run your tests with "python3 -m pytest". 
# If it's not installed, run "pip3 install -r requirements.txt"