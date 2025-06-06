class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...

    @abstractmethod
    def calculate_perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):
    # Implementation of Triangle
    pass


if __name__ == "__main__":
    rec = Rectangle(10, 5)
    print(rec.calculate_area())
    print(rec.calculate_perimeter())