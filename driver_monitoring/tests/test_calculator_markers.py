import pytest
from driver_monitoring.calculator import Calculator

# Using markers
calc = Calculator()

@pytest.mark.smoke
def test_add():
    assert calc.add(2, 4) == 6
    assert calc.add(-1, 5) == 4
    assert calc.add(0, 0) == 0

@pytest.mark.smoke
def test_subtract():
    assert calc.subtract(2, 4) == -2
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 0) == 0

@pytest.mark.regression
def test_multiply():
    assert calc.multiply(2, 5) == 10
    assert calc.multiply(3, 3) == 9
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(0, 100) == 0

@pytest.mark.regression
def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    assert calc.divide(5, 2) == 2.5

@pytest.mark.edge
def test_divide_by_zero():
    assert calc.divide(10, 0) == "Error! Division by zero."
