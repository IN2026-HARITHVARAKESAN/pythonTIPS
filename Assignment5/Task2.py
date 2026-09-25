"""Swapping two numbers with using a third variable."""

def swap_numbers(a: int, b: int) -> None:
    """Swap two numbers using a third variable."""
    print(f"Before swapping: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    swap_numbers(first_number, second_number)