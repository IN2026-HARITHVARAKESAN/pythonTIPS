import unittest
from unittest.mock import Mock

from Task1 import Calculator

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(Calculator().subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(Calculator().multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(Calculator().divide(6, 3), 2)

    def test_divide_by_zero_prints_error_and_returns_none(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator().divide(10, 0)

if __name__ == "__main__":
    unittest.main()
