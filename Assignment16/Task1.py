"""Simple calculator functions"""
def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y"""
    return x - y

def multiply(x, y):
    """Returns the product of x and y"""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y"""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculate(operation, x, y):
    """Performs the operation on x and y"""
    return operation(x, y)

if __name__ == "__main__":
    print("Addition:", calculate(add, 10, 5))
    print("Subtraction:", calculate(subtract, 10, 5))
    print("Multiplication:", calculate(multiply, 10, 5))
    print("Division:", calculate(divide, 10, 5))