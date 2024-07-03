"""Polymorphism is based on the greek words Poly (many) and morphism (forms). We will create a structure that can
take or use many forms of objects. Polymorphism is an ability (in OOP) to use a common interface for multiple forms (
data types). Example 1: The student can act as a student in college, act as a player on the ground,
and as a daughter/brother in the home. Example 2: In the programming language, the + operator, acts as a
concatenation and arithmetic addition. Example 3: If we need to color a shape, there are multiple shape options (
rectangle, square, circle). However we could use the same method to color any shape.z
"""


class MyList:
    """Operator Overloading: as we know + operator is used for concatenation and arithmetic operations in case of,
    Numeric Values.
    Not If we apply + operator for two list it just concatenate two list, but what if we want to perform arithmetic
    operation on each respective element of list then we can use operator overloading example,
    Given Below"""

    def __init__(self, value):
        if isinstance(value, list):
            self.__value = value
        else:
            raise Exception("Please create a List Object")

    def __add__(self, other):
        """__add__: + operator overloading"""
        if isinstance(other, list):
            if len(self.__value) == len(other):
                result = []
                for i in range(len(self.__value)):
                    if self.__value[i].__class__ == other[i].__class__:
                        result.append(self.__value[i] + other[i])
                return result
            else:
                print("List Should be Same Length")
        else:
            raise Exception("Required List for This Operation")

    def __sub__(self, other):
        """__sub__: - operator overloading"""
        if isinstance(other, list):
            if len(self.__value) == len(other):
                result = []
                for i in range(len(self.__value)):
                    if self.__value[i].__class__ == other[i].__class__:
                        result.append(self.__value[i] - other[i])
                return result
            else:
                print("List Should be Same Length")
        else:
            raise Exception("Required List for This Operation")

    def __mul__(self, other):
        """__mul__: * operator overloading"""
        if isinstance(other, list):
            if len(self.__value) == len(other):
                result = []
                for i in range(len(self.__value)):
                    if self.__value[i].__class__ == other[i].__class__:
                        result.append(self.__value[i] * other[i])
                return result
            else:
                print("List Should be Same Length")
        else:
            raise Exception("Required List for This Operation")

    def __truediv__(self, other):
        """__truediv__: / operator overloading"""
        if isinstance(other, list):
            if len(self.__value) == len(other):
                result = []
                for i in range(len(self.__value)):
                    if self.__value[i].__class__ == other[i].__class__:
                        result.append(self.__value[i] / other[i])
                return result
            else:
                print("List Should be Same Length")
        else:
            raise Exception("Required List for This Operation")

    def __floordiv__(self, other):
        """__floordiv__: // operator overloading"""
        if isinstance(other, list):
            if len(self.__value) == len(other):
                result = []
                for i in range(len(self.__value)):
                    if self.__value[i].__class__ == other[i].__class__:
                        result.append(self.__value[i] // other[i])
                return result
            else:
                print("List Should be Same Length")
        else:
            raise Exception("Required List for This Operation")


if __name__ == "__main__":
    print("Operator +")
    print(5 + 6)
    print("Hello" + ", World~")
    print((1, 2, 3) + (4, 5, 6))
    print([1, 2, 3] + [4, 5, 6])
    print(
        "Behind the scene __add__ method is used to perform such functionality\n"
        "Now Lets override this operator functionality now it perform arithmetic operation in each respective list "
        "element."
    )
    lst = MyList([1, 2, 3, 4])
    print(lst + [1, 2, 3, 4])
