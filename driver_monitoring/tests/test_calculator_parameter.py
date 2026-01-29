import pytest
from driver_monitoring.calculator import Calculator

# Using Parametrize test
calc = Calculator()

@pytest.mark.parametrize("x, y, expected", [
    (2, 4, 6),
    (-1, 5, 4),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert calc.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 4, -2),
    (10, 5, 5),
    (0, 0, 0),
])
def test_subtract(x, y, expected):
    assert calc.subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 5, 10),
    (-3, 3, -9),
    (0, 100, 0),
])
def test_multiply(x, y, expected):
    assert calc.multiply(x, y) == expected
  
@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 2, 2.5),
])
def test_divide(x, y, expected):
    assert calc.divide(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 0, "Error! Division by zero."),
    (0, 0, "Error! Division by zero."),
])
def test_divide_by_zero(x, y, expected):
    assert calc.divide(x, y) == expected
