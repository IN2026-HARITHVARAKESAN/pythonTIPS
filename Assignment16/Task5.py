"""This file demonstrates the use of descriptors in Python."""
class UpperCase:
    """A descriptor that converts string values to uppercase."""
    def __get__(self, instance, owner):
        """Return the uppercase version of the name."""
        return instance._name

    def __set__(self, instance, value):
        """Set the name to the uppercase version."""
        instance._name = value.upper()


class Person:
    """A class representing a person with a name."""
    name = UpperCase()

if __name__ == "__main__":
    person = Person()

    person.name = "harith"

    print(person.name)
