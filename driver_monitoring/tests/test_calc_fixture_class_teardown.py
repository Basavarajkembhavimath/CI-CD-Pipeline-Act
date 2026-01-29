import pytest
from driver_monitoring.calculator import Calculator

# Fixture with scope= 'class' and teardown
@pytest.fixture(scope="class")
def calc():
    print("\n[Setup] Creating Calculator instance for the class...")
    calc_instance = Calculator()
    yield calc_instance
    print("\n[Teardown] Cleaning up Calculator instance after class tests....")


class TestCalculator:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5

    def test_subtract(self, calc):
        assert calc.subtract(10, 5) == 5

    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5

    def test_divide_by_zero(self, calc):
        assert calc.divide(10, 0) == "Error! Division by zero."

    # def test_add(self, calc):
    #     assert calc.add(2, 10) == 12