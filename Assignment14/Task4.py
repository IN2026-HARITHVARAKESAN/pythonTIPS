"""This module contains unit tests for the Calculator class defined in Task1.py."""
import unittest
from unittest.mock import Mock

from Assignment14.Task1 import Calculator

class CalculatorTests(unittest.TestCase):
    """Unit tests for the Calculator class defined in Task1.py."""
    def setUp(self):
        """Set up the test environment and initialize the Calculator instance."""
        self.calculator = Calculator()

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

    def test_check_history(self):
        """Test that the history is initially empty."""
        self.assertEqual(self.calculator.get_history(), [])

    def test_add_history(self):
        """Test that the add method records the operation in history."""
        self.calculator.add(5, 3)

        expected = [
           {
                "operation": "Add",
                "inputs": [5, 3],
                "result": 8
            }
        ]

        self.assertEqual(self.calculator.get_history(), expected)

    def test_history_returns_copy(self):
        """Test that the get_history method returns a copy of the history."""
        self.calculator.add(5, 3)
        history = self.calculator.get_history()

        history.append({"operation": "Other", "inputs": [], "result": None})

        self.assertEqual(len(self.calculator.get_history()), 1)

    def test_advanced_operation_uses_service_result(self):
        """Test that the advanced_operation method uses the provided service and returns the expected result."""
        service = Mock()
        service.calculate.return_value = 3

        calculator = Calculator(advanced_service=service)

        result = calculator.advanced_operation("root", 9)

        self.assertEqual(result, 3)
        service.calculate.assert_called_once_with("root", 9)

        history = calculator.get_history()
        self.assertEqual(history[0]["operation"], "root")
        self.assertEqual(history[0]["inputs"], [9])
        self.assertEqual(history[0]["result"], 3)

    def test_advanced_operation_without_service(self):
        """Test that the advanced_operation method returns None when no service is provided."""
        result = self.calculator.advanced_operation("root", 9)

        self.assertIsNone(result)
        self.assertEqual(self.calculator.get_history(), [])

if __name__ == "__main__":
    unittest.main()
