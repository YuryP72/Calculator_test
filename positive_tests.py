import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        """Умножение"""
        assert self.calc.multiply(self, 1,5) == 5

    def test_division_calculate_correctly(self):
        """Деление"""
        assert self.calc.division(self, 2, 2) == 1

    def test_adding_calculate_correctly(self):
        """Сложение"""
        assert self.calc.adding(self, 5, 5) == 10

    def test_substraction_calculate_correctly(self):
        """Вычитание"""
        assert self.calc.subtraction(self, 3, 3) == 0