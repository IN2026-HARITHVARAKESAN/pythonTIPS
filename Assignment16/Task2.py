"""Defines a function `make_multiplier` that takes an integer `n` and returns a new function `multiplier`. The `multiplier` function takes an integer `x` and returns the product of `x` and `n`."""
def make_multiplier(n):
    """Returns a function that multiplies its input by n."""
    def multiplier(x):
        return x * n

    return multiplier

if __name__ == "__main__":
    doubler = make_multiplier(2)
    tripler = make_multiplier(3)
    print("Doubler:", doubler(5))
    print("Doubler:", doubler(10))

    print("Tripler:", tripler(5))
    print("Tripler:", tripler(10))