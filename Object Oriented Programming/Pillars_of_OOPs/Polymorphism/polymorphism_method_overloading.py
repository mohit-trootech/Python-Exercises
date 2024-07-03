"""Polymorphism is based on the greek words Poly (many) and morphism (forms). We will create a structure that can
take or use many forms of objects. Polymorphism is an ability (in OOP) to use a common interface for multiple forms (
data types). Example 1: The student can act as a student in college, act as a player on the ground,
and as a daughter/brother in the home. Example 2: In the programming language, the + operator, acts as a
concatenation and arithmetic addition. Example 3: If we need to color a shape, there are multiple shape options (
rectangle, square, circle). However we could use the same method to color any shape.z
"""

from multipledispatch import dispatch


class MethodOverload:
    """Method Overloading: Method overloading in Python is a concept that allows a class to have multiple methods
    with the same name but different parameter lists. Unlike other programming languages like Java, Python does not
    directly support method overloading, where you can define multiple methods with different parameter lists.
    """

    def __init__(self):
        pass

    @dispatch(int, int)
    def concat(self, value1, value2):
        return value1 + value2

    @dispatch(int, int, int)
    def concat(self, value1, value2, value3):
        return value1 + value2 + value3

    # @dispatch(list)
    # def concat(self, *args):
    #     print("This one", args)
    #     return sum(args)


if __name__ == "__main__":
    """Python's standard library doesn't have any other provision for implementing method overloading. However,
    we can use a dispatch function from a third-party module named MultipleDispatch for this purpose.
    First, you need to install the Multipledispatch module using the following command
    ```pip install multipledispatch```−
    """
    obj = MethodOverload()
    print(obj.concat(1, 2, 3))
    print(obj.concat(2, 3))
    # print(obj.concat(2, 3, 4, 5, 6, 7))
