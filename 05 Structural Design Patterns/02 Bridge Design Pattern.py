# The implementation hierarchy

from abc import ABC, abstractmethod


# Implementation interface
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        ...


# Concreate implementations

class Red(Color):
    def apply_color(self):
        return "RED"


class Blue(Color):
    def apply_color(self):
        return "BLUE"


# The abstraction hierarchy -> Shape

# Abstraction

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        ...


# Refined Abstractions
class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color.apply_color()} Circle"


class Rectangle(Shape):
    def draw(self):
        return f"Drawing a {self.color.apply_color()} Rectangle"


# Client Code

if __name__ == "__main__":
    red = Red()
    blue = Blue()

    red_circle = Circle(red)
    blue_rectangle = Rectangle(blue)

    print(red_circle.draw())
    print(blue_rectangle.draw())
