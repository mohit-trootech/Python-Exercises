"""
Python Exercise to find the Area and Perimeter of Shapes using Class Concepts
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length: float, breadth: float) -> None:
        """
        rectangle constructor for self.length and self.breadth
        """
        self.length = length
        self.breadth = breadth

    def area(self) -> None:
        """
        method to find area of rectangle object
        """
        return "Area of Rectangle with Length & Breadth {} & {} = {:.2f}".format(
            self.length, self.breadth, self.length * self.breadth
        )

    def perimeter(self) -> None:
        """
        method to find perimeter of rectangle object
        """
        return "Perimeter of Rectangle with Length & Breadth {} & {} = {:.2f}".format(
            self.length, self.breadth, 2 * (self.length + self.breadth)
        )


class Square(Shape):

    def __init__(self, side: float) -> None:
        """
        square constructor for self.side
        """
        self.side = side

    def area(self) -> None:
        """
        method to find area of square object
        """
        return "Area of Square with Side {} = {:.2f}".format(self.side, self.side**2)

    def perimeter(self) -> None:
        """
        method to find perimeter of square object
        """
        return "Perimeter of Square with Side {} = {:.2f}".format(
            self.side, 4 * self.side
        )


class Circle(Shape):

    def __init__(self, radius: float) -> None:
        """
        Circle constructor for self.radius
        """
        self.radius = radius

    def area(self) -> None:
        """
        method to find area of circle object
        """
        return "Area of Circle with Radius {} = {:.2f}".format(
            self.radius, pi * self.radius**2
        )

    def perimeter(self) -> None:
        """
        method to find perimeter of circle object
        """
        return "Perimeter of Circle with Radius {} = {:.2f}".format(
            self.radius, 2 * pi * self.radius
        )


class Triangle(Shape):

    def __init__(self, base: float, height: float) -> None:
        """
        Triangle constructor for self.base, self.height
        """
        self.base = base
        self.height = height

    def area(self) -> None:
        """
        method to find area of triangle object
        """
        return "Area of Triangle with Radius {} and Height {} = {:.2f}".format(
            self.base, self.height, (self.base * self.height) / 2
        )

    def perimeter(self):
        pass


print("Choose Shape".center(50, "-"))
try:
    option = float(input("1. Rectangle\n" "2. Square\n" "3. Circle\n4. Height: "))
    if option == 1.0:
        length = float(input("Enter Length of Rectangle: "))
        breadth = float(input("Enter Breadth of Rectangle: "))
        obj_rect = Rectangle(abs(length), abs(breadth))
        print(obj_rect.area())
        print(obj_rect.perimeter())
    elif option == 2.0:
        side = float(input("Enter Side of Square: "))
        obj_sq = Square(abs(side))
        print(obj_sq.area())
        print(obj_sq.perimeter())
    elif option == 3.0:
        radius = float(input("Enter Radius of Circle: "))
        obj_circle = Circle(abs(radius))
        print(obj_circle.area())
        print(obj_circle.perimeter())
    elif option == 4.0:
        base = float(input("Enter Base of Triangle: "))
        height = float(input("Enter Height of Triangle: "))
        obj_circle = Triangle(abs(base), abs(height))
        print(obj_circle.area())
        print(obj_circle.perimeter())
    else:
        print("Try Again with Valid Input".center(50, "-"))

except ValueError as ve:
    print("Enter a Number Input", ve)
