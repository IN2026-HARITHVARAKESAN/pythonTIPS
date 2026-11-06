from datetime import datetime
import unittest
from unittest.mock import Mock

from Task1 import Calculator


class CalculatorTests(unittest.TestCase):
    log_file = "test_results.log"

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        with open(self.log_file, "a") as log:
            log.write(f"{self.id()} | {'pass' if self._outcome.success else 'fail'} | {datetime.now()}\n")

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_divide_by_zero_prints_error_and_returns_none(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator().divide(10, 0)

    def test_advanced_operation_uses_service_result(self):
        service = Mock()
        service.calculate.return_value = 3
        self.calculator = Calculator(advanced_service=service)

        self.assertEqual(self.calculator.advanced_operation("root", 9), 3)
        service.calculate.assert_called_once_with("root", 9)


if __name__ == "__main__":
    unittest.main()