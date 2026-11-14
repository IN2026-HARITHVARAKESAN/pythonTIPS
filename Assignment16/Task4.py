"""This code demonstrates the use of metaclasses in Python."""
class GreetingMetaclass(type):
    """A metaclass that adds a greet method to classes."""
    def __new__(mcs, name, bases, attrs):
        """Add a greet method to the class."""
        def greet(self):
            """Prints a greeting message."""
            print("Hello! Welcome!")

        attrs["greet"] = greet

        return super().__new__(mcs, name, bases, attrs)


class Student(metaclass=GreetingMetaclass):
    """A class representing a student."""
    def study(self):
        """Prints a message that the student is studying."""
        print("Student is studying")


class Teacher:
    """A class representing a teacher."""
    def teach(self):
        """Prints a message that the teacher is teaching."""
        print("Teacher is teaching")

if __name__ == "__main__":
    student = Student()
    teacher = Teacher()

    student.study()
    student.greet()

    teacher.teach()

    try:
        teacher.greet()
    except AttributeError as error:
        print("Error:", error)
