"""This file demonstrates the method resolution order (MRO) in Python using multiple inheritance."""
class A:
    """A base class with a show method."""
    def show(self):
        """Prints a message indicating the class."""
        print("Class A")

class B(A):
    """A subclass of A.""" 
    def show(self):
        """Prints a message indicating the class."""
        print("Class B")

class C(A):
    """A subclass of A."""  
    def show(self):
        """Prints a message indicating the class."""
        print("Class C")

class D(B, C):
    """A subclass of B and C demonstrating multiple inheritance."""
    def hide(self):
        """Prints a message indicating the class."""
        print("Class D")

class E(C, B):
    """A subclass of C and B demonstrating multiple inheritance."""
    def hide(self):
        """Prints a message indicating the class."""
        print("Class E")
if __name__ == "__main__":
    obj = D()

    print("First MRO:")

    obj.show()
    obj2 = E()

    print("\nSecond MRO:")
    obj2.show()