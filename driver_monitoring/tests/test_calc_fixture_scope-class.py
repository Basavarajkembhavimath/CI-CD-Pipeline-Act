import pytest
from driver_monitoring.calculator import Calculator


# Fixture with scope = "class"
@pytest.fixture(scope='class')
def calc():
    print("\nSetting up calculator instance for the whole class...")
    return Calculator()

# Group tests inside a class
class TestCalculator:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5

    def test_subtract(self, calc):
        assert calc.subtract(10, 5) == 5

    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5

    def test_divide_fraction(self, calc):
        assert calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self, calc):
        assert calc.divide(10, 0) == "Error! Division by zero."