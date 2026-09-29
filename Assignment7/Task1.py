"""Implements a exception handling for error in the given code division"""

import random

def risky_calculation():

    number = random.randint(-10, 10)

    return 100 / number

try:
    for _ in range(1000):
        risky_calculation()
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")