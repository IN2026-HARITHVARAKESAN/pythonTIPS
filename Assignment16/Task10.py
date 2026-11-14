"""This module contains two decorators: `profile_execution` and `log_function_call`."""
import time
from datetime import datetime
from functools import wraps

def profile_execution(func):
    """A decorator that profiles the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"{func.__name__} took {execution_time:.6f} seconds")

        return result

    return wrapper

def log_function_call(func):
    """A decorator that logs the function call details to a file."""
    @wraps(func)
    def wrapper(*args, **kwargs):

        call_time = datetime.now()

        result = func(*args, **kwargs)

        with open("Assignment16/function_log.txt", "a", encoding="utf-8") as file:
            file.write(f"Function: {func.__name__}\n")
            file.write(f"Arguments: {args}\n")
            file.write(f"Keyword Arguments: {kwargs}\n")
            file.write(f"Return Value: {result}\n")
            file.write(f"Call Time: {call_time}\n")

        return result

    return wrapper

@profile_execution
@log_function_call
def add_numbers(a, b):
    """A function that adds two numbers."""
    time.sleep(1)
    return a + b

@profile_execution
@log_function_call
def calculate_total(name, price, quantity):
    """A function that calculates the total amount for a given item."""
    time.sleep(2)
    total = price * quantity
    return f"{name}'s total amount is {total}"

if __name__ == "__main__":
    print("Calling add_numbers:")
    result1 = add_numbers(10, 20)
    print("Result:", result1)

    print("\nCalling calculate_total:")
    result2 = calculate_total("Laptop", 50000, 2)
    print("Result:", result2)