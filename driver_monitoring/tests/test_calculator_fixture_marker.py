import pytest
from driver_monitoring.calculator import Calculator

#-----------------------------------
# Fixture: reusable Calcultor object
#-----------------------------------

@pytest.fixture(scope="module")
def calc():
    print("\nSetting up Calculator instance....")
    return Calculator()

#------------------------------------
# Smoke tests (basic functionality)
#------------------------------------

@pytest.mark.smoke
@pytest.mark.parametrize("x, y, expected", [
    (2, 4, 6),
    (-1, 5, 4),
    (0, 0, 0),
]) 
def test_add(calc, x, y, expected):
    assert calc.add(x, y) == expected

@pytest.mark.smoke
@pytest.mark.parametrize("x, y, expected", [
    (4, 2, 2),
    (2, 4, -2),
    (0, 0, 0),
])
def test_substract(calc, x, y, expected):
    assert calc.subtract(x, y) == expected

# -----------------------------------
# Regression tests(deeper validation)
# -----------------------------------

@pytest.mark.regression
@pytest.mark.parametrize("x, y, expected", [
    (2, 5, 10),
    (-3, -3, 9),
    (0, 100, 0),
])
def test_multiply(calc, x, y, expected):
    assert calc.multiply(x, y) == expected

@pytest.mark.regression 
@pytest.mark.parametrize("x, y, expected", [ 
    (10, 2, 5), 
    (9, 3, 3), 
    (5, 2, 2.5), 
]) 
def test_divide(calc, x, y, expected): 
    assert calc.divide(x, y) == expected


@pytest.mark.edge
@pytest.mark.parametrize("x, y, expected", [
    (9, 3, 3),
    (10, 0, "Error! Division by zero."),
])
def test_divide_by_zero(calc, x, y, expected):
    assert calc.divide(x, y) == expected
