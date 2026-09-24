"""This file contains expression_evaluator() which evaluates a mathematical expression with a given string and returns the result."""

from unittest import result


def expression_evaluator(expression: str) -> float:
    """Evaluate a mathematical expression with a given string and return the result"""
    result = eval(expression)
    return result

if __name__ == "__main__":
    given_input = input("enter a mathematical expression to evaluate: ")
    result = expression_evaluator(given_input)
    print(f"The result of the expression is: {result}")