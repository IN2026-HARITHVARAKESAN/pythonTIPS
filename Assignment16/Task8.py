"""This file defines the concept of polymorphism in Python, where different classes can be treated as instances of the same type through a common interface."""
class Duck:
    """A class representing a duck with a quack method."""
    def quack(self):
        """Prints the sound a duck makes."""
        print("Duck:Quack! Quack!")

class Person:
    """A class representing a person with a quack method."""
    def quack(self):
        """Prints a message indicating the person is imitating a duck."""
        print("Person:A person is imitating a duck: Quack!")

class Dog:
    """A class representing a dog with a bark method."""
    def bark(self):
        """Prints the sound a dog makes."""
        print("Dog:Woof! Woof!")

def make_it_quack(duck):
    """A function that takes an object and calls its quack method if it exists."""
    duck.quack()

if __name__ == "__main__":
    duck = Duck()
    person = Person()
    dog = Dog()

    make_it_quack(duck)
    make_it_quack(person)
    try:
        make_it_quack(dog)
    except Exception as e:
        print(f"Error: {e}")