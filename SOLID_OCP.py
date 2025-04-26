from abc import ABC, abstractmethod

# BAD VERSION - violates OCP:
class AreaCalculatorBad:
    def area(self, shape):
        if isinstance(shape, CircleBad):
            return 3.14159 * shape.radius**2
        elif isinstance(shape, RectangleBad):
            return shape.width * shape.height

class CircleBad:
    def __init__(self, radius):
        self.radius = radius

class RectangleBad:
    def __init__(self, width, height):
        self.width = width
        self.height = height


# GOOD VERSION:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def area(self, shape):
        return shape.area()