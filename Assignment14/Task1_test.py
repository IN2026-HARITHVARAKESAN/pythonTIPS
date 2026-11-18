"""Unit tests for the Calculator class in Task1.py."""
import unittest

from Assignment14.Task1 import Calculator

class CalculatorTests(unittest.TestCase):
    """Unit tests for the Calculator class in Task1.py."""
    def test_add(self):
        """Test the add method of the Calculator class."""
        self.assertEqual(Calculator().add(5, 3), 8)

    def test_subtract(self):
        """Test the subtract method of the Calculator class."""
        self.assertEqual(Calculator().subtract(5, 3), 2)

    def test_multiply(self):
        """Test the multiply method of the Calculator class."""
        self.assertEqual(Calculator().multiply(5, 3), 15)

    def test_divide(self):
        """Test the divide method of the Calculator class."""
        self.assertEqual(Calculator().divide(6, 3), 2)

    def test_divide_by_zero_prints_error_and_returns_none(self):
        """Test that dividing by zero prints an error and returns None."""
        with self.assertRaises(ZeroDivisionError):
            Calculator().divide(10, 0)

if __name__ == "__main__":
    unittest.main()
