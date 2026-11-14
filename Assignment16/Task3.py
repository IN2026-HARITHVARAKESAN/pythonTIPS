"""Optimize the calculation of Fibonacci numbers."""
def cache(func):
    """A decorator that caches the results of a function."""
    results = {}

    def wrapper(n):
        """Check if the result is already cached; if not, compute and cache it."""
        if n in results:
            print("Fetching from cache:", n)
            return results[n]

        print("Calculating:", n)
        result = func(n)
        results[n] = result

        return result

    return wrapper


@cache
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Fibonacci of 10:", fibonacci(10))
    print("Fibonacci of 10 again:", fibonacci(10))

    print("Fibonacci of 100:", fibonacci(100))