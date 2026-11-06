class Calculator:
    def __init__(self, advanced_service=None):
        self.advanced_service = advanced_service
        self.history = []

    def _record_history(self, operation, inputs, result):
        self.history.append({
            "operation": operation,
            "inputs": inputs,
            "result": result
        })

    def get_history(self):
        return self.history.copy()

    def add(self, a, b):
        result = a + b
        self._record_history("Add", [a, b], result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._record_history("Subtract", [a, b], result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._record_history("Multiply", [a, b], result)
        return result

    def divide(self, a, b):
        if b == 0:
            self._record_history("Divide", [a, b], None)
            return None
        result = a / b
        self._record_history("Divide", [a, b], result)
        return result
    
    def divide(self, a, b):
        if self.is_zero(b):
            raise ZeroDivisionError("Denominator can't be zero.")
        return a / b

    def is_zero(self, num):
        return num == 0
    
    def advanced_operation(self, operation, value):
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