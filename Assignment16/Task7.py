"""This module demonstrates the use of a mixin class to provide JSON serialization functionality to other classes."""
import json

class JsonSerializableMixin:
    """A mixin class that provides a method to serialize an object to JSON."""
    def to_json(self):
        """Convert the object to a JSON string."""
        return json.dumps(self.__dict__)


class Student(JsonSerializableMixin):
    """A class representing a student, inheriting from JsonSerializableMixin."""
    def __init__(self, name, age, course):
        """Initialize the Student with name, age, and course."""
        self.name = name
        self.age = age
        self.course = course

if __name__ == "__main__":
    student = Student("Harith", 25, "Python")
    result = student.to_json()
    print(result)