"""This file contains a function classify_number(number: int) -> str which classifies a number as 'positive', 'negative', or 'zero' based on its value, factorial(n: int) -> int which calculates the factorial of an integer n."""

def classify_number(number: int) -> str:
    """Classify a number as 'positive', 'negative', or 'zero' based on its value"""
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def factorial(n: int) -> int:
    """Calculate the factorial of an integer n"""
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    given_input = input("enter a number: ")
    number = int(given_input)
    classification = classify_number(number)
    print(f"The number {number} is a {classification}")

    given_input = input("enter a non-negative integer to calculate its factorial: ")
    n = int(given_input)
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = factorial(n)
        print(f"The factorial of {n} is: {fact}")