import pytest
from calculator import add, subtract, multiply, divide 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 1) == 4
    assert subtract(3, 3) == 0

def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ValueError):
        divide(5, 0)