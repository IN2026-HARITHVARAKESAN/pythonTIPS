"""This script demonstrates the use of a dictionary in Python to store and display student information."""
if __name__ == "__main__":
    student = {}

    student["name"] = "Harith"
    student["age"] = 25
    student["city"] = "Chennai"

    print("Dictionary contents:")

    for key, value in student.items():
        print(key, ":", value)