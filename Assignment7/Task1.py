"""Implements a exception handling for error in the given code division"""

import random

def risky_calculation():
    """Performs a risky calculation that may raise a ZeroDivisionError"""
    number = random.randint(-10, 10)

    return 100 / number

if __name__ == "__main__":
    try:
        for _ in range(1000):
            risky_calculation()
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")