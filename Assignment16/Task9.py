"""This module defines an abstract base class `Shape` and its subclasses `Circle`, `Rectangle`, and `Triangle`."""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """An abstract base class representing a geometric shape."""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""
    def __init__(self, radius):
        """Initialize the Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        """Initialize the Rectangle with a length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

class Triangle(Shape):
    """A class representing a triangle, inheriting from Shape."""
    def __init__(self, a, b, c):
        """Initialize the Triangle with three sides."""
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.a + self.b + self.c

    def area(self):
        """Calculate the area of the triangle."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(10, 5)
    triangle = Triangle(3, 4, 5)

    print("Circle")
    print("Area:", round(circle.area(), 2))
    print("Perimeter:", round(circle.perimeter(), 2))

    print("\nRectangle")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    print("\nTriangle")
    print("Area:", triangle.area())
    print("Perimeter:", triangle.perimeter())