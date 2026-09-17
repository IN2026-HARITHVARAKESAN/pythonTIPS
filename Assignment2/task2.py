"""This file contains filter_primes(numbers: List[int]) -> List[int] method which filters prime numbers from a list of integers and returns a list of prime numbers,invert_dict(input_dict: Dict[Any, Any]) -> Dict[Any, List[Any]] method which return a dictionary with keys and values inverted"""

from typing import Any, List


def filter_primes(numbers: List[int]) -> List[int]:
    """Filter prime numbers from a list of integers and return a list of prime numbers"""
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

def invert_dict(input_dict: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """Return a dictionary with keys and values inverted"""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict

if __name__ == "__main__":
    given_input = input("enter a list of integers separated by spaces: ")
    numbers = [int(x) for x in given_input.split()]
    primes = filter_primes(numbers)
    print(f"The prime number in the list are: {primes}")

    given_input = input("enter a dictionary in the format key1:value1,key2:value2,...: ")
    input_dict = {}
    for pair in given_input.split(','):
        key, value = pair.split(':')
        input_dict[key] = value
    inverted = invert_dict(input_dict)
    print(f"The inverted dictionary is: {inverted}")