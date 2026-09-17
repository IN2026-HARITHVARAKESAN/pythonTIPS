"""This file contains reverse_words(input_str: str) which reverses letters in each word,solve_quad(a: float, b: float, c: float) -> Tuple[float, float] which solves a quadratic equation and evaluate_conditions(a: bool, b: bool, c: bool) -> bool which evaluates the conditions a, b, c and returns True if two are True, else False"""


def reverse_words(input_str:str) -> str:
    """Reverse a string with each words reveresed"""
    words= input_str.split()
    reversed_words= []
    for word in words:
        reversed_words.append(word[::-1])
    result = " ".join(reversed_words)
    return result

def solve_quad(a: float, b: float, c: float) -> Tuple[float, float]:
    """Solve a quadratic equation of ax^2 + bx + c = 0"""
    quadratic = b * b - 4 * a * c
    if quadratic < 0:
        return None
    root1 = (-b + quadratic**0.5) / (2*a)
    root2 = (-b - quadratic**0.5) / (2*a)
    return (root1, root2)
def evaluate_conditions(a: bool, b: bool, c: bool) -> bool:
    """Evaluate the conditions a, b, c and return True if two are True, else False"""
    return (a and b) or (a and c) or (b and c)

if __name__ == "__main__":
    given_input = input("enter a words to reverse: ")
    print(reverse_words(given_input))

    given_input = input("enter a, b, c for quadratic equation: ")
    a, b, c = given_input.split()
    roots = solve_quad(float(a), float(b), float(c))
    print(f"The roots of the quadratic equation are: {roots}")

    given_input = input("enter values for a, b, c (boolean) values should be 'true' or 'false': ")
    a, b, c = given_input.split()
    a = a.lower() == 'true'
    b = b.lower() == 'true'
    c = c.lower() == 'true'
    result = evaluate_conditions(a, b, c)
    print(f"The result of evaluating the conditions is: {result}")