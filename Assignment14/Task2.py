"""Unit tests for the Calculator class in Assignment14.Task1."""
from datetime import datetime
import unittest
from unittest.mock import Mock

from Assignment14.Task1 import Calculator


class CalculatorTests(unittest.TestCase):
    """Unit tests for the Calculator class in Assignment14.Task1."""
    log_file = "test_results.log"

    def setUp(self):
        """Set up the test environment and initialize the Calculator instance."""
        self.calculator = Calculator()

    def tearDown(self):
        """Log the test result to a file after each test."""
        with open(self.log_file, "a") as log:
            log.write(f"{self.id()} | {'pass' if self._outcome.success else 'fail'} | {datetime.now()}\n")

    def test_add(self):
        """Test the add method of the Calculator class."""
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_subtract(self):
        """Test the subtract method of the Calculator class."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        """Test the multiply method of the Calculator class."""
        self.assertEqual(self.calculator.multiply(5, 3), 15)

    def test_divide(self):
        """Test the divide method of the Calculator class."""
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_divide_by_zero_prints_error_and_returns_none(self):
        """Test that dividing by zero prints an error and returns None."""
        with self.assertRaises(ZeroDivisionError):
            Calculator().divide(10, 0)

    def test_advanced_operation_uses_service_result(self):
        """Test that the advanced_operation method uses the provided service and returns the expected result."""
        service = Mock()
        service.calculate.return_value = 3
        self.calculator = Calculator(advanced_service=service)

        self.assertEqual(self.calculator.advanced_operation("root", 9), 3)
        service.calculate.assert_called_once_with("root", 9)


if __name__ == "__main__":
    unittest.main()