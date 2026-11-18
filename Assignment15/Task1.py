
"""Check numbers for primality and generate prime numbers."""

def is_prime(number):
    """Return whether number is prime"""
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def prime_generator():
    """Yield prime numbers in ascending order infinitely."""
    number = 2

    while True:
        if is_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
    generator = prime_generator()

    for count in range(100):
        print(next(generator))