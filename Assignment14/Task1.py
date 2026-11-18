"""A simple calculator class that supports basic arithmetic operations and maintains a history of calculations."""
class Calculator:
    """A simple calculator class that supports basic arithmetic operations and maintains a history of calculations."""
    def __init__(self, advanced_service=None):
        self.advanced_service = advanced_service
        self.history = []

    def _record_history(self, operation, inputs, result):
        """Record the operation, inputs, and result in the history."""
        self.history.append({
            "operation": operation,
            "inputs": inputs,
            "result": result
        })

    def get_history(self):
        """Return a copy of the calculation history."""
        return self.history.copy()

    def add(self, a, b):
        """Add two numbers and record the operation in history."""
        result = a + b
        self._record_history("Add", [a, b], result)
        return result

    def subtract(self, a, b):
        """Subtract two numbers and record the operation in history."""
        result = a - b
        self._record_history("Subtract", [a, b], result)
        return result

    def multiply(self, a, b):
        """Multiply two numbers and record the operation in history."""
        result = a * b
        self._record_history("Multiply", [a, b], result)
        return result

    def divide(self, a, b):
        """Divide two numbers and record the operation in history. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            self._record_history("Divide", [a, b], None)
            return None
        result = a / b
        self._record_history("Divide", [a, b], result)
        return result

    def is_zero(self, num):
        """Check if a number is zero."""
        return num == 0
    
    def advanced_operation(self, operation, value):
        """Perform an advanced operation using the provided service and record it in history."""
        if self.advanced_service is None:
            return None
        result = self.advanced_service.calculate(operation, value)
        self._record_history(operation, [value], result)
        return result

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(5, 3))
    print("Multiplication:", calc.multiply(5, 3))
    print("Division:", calc.divide(5, 3))