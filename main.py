"""Main script demonstrating the usage of various tools from the TechFellowTools and TechFellowPlugins packages."""
from TechFellowTools.math_tools import calculate_mean, matrix_addition
from TechFellowTools.string_tools import is_palindrome, reverse_words
from TechFellowTools.data_tools import group_by_column
from TechFellowTools import find_shortest_path

if __name__ == "__main__":
    print("Mean:", calculate_mean([10, 20, 30, 40]))

    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    print("Matrix Addition:", matrix_addition(matrix_a, matrix_b))

    print("Palindrome:", is_palindrome("madam"))
    print("Reversed Words:", reverse_words("Welcome to Python"))

    employees = [
        {"name": "Arun", "department": "IT"},
        {"name": "Bala", "department": "HR"},
        {"name": "Charan", "department": "IT"}
    ]

    print("Grouped Employees:", group_by_column(employees, "department"))

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"]
    }

    print("Shortest Path:", find_shortest_path(graph, "A", "D"))