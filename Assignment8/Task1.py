"""Square and print the values of prime numbers in a list by fetching the data from json file."""

import json

import random
def is_prime(value):
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def square_prime_values(data):
    return [json_data["value"] ** 2 for json_data in data if is_prime(json_data["value"])]

if __name__ == '__main__':
    data = [{'id': i, 'value': random.randint(1, 100)} for i in range(1, 10001)]
    json.dump(data, open('data.json', 'w'))
    print(f'squared prime values: {square_prime_values(data)}, Unique squared prime values:  {set(square_prime_values(data))}')