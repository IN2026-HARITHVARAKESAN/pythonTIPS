"""Creates a new custom exception called InvalidAgeException. This exception is raised when the user enters an invalid age (less than or equal to 0)."""

class InvalidAgeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        age = int(input("Enter your valid age above zero: "))
        print(f"is it valid age? {validate_user_age(age)}")
        pass

def validate_user_age(age):

    if age <= 0:
        raise InvalidAgeException("Age must be a positive integer.")
    if age < 13:
        return False
    else:
        return True

if __name__ == "__main__":
    age = int(input("Enter your age: "))
    if validate_user_age(age):
        print("You are eligible.")
    else:
        print("You are not eligible.")
