"""In Python, encapsulation is a method of wrapping data and functions into a single entity. For example,
A class encapsulates all the data (methods and variables). Encapsulation means the internal representation of an
object is generally hidden from outside of the object’s definition."""


class Capsule:
    """sample class to implement encapsulation. In Encapsulation:  we can restrict access to methods and variables.
    This prevents data from direct modification which is called encapsulation. In Python, we denote private
    attributes using underscore as the prefix i.e single _ or double __.
    """

    __capsule_class = "Sample Class Attribute"  # Private Class Attribute
    _protected = "I am Protected"
    public = "I am Public"

    def __init__(self):
        """
        Access Specifier:Access specifiers in Python have an important role to play in securing data from
        unauthorized access and in preventing it from being exploited.
        """
        self.__capsule_instance = None  # Private Instance Attribute

    @property
    def instance_property(self):
        """property decorator is the simple way to fetch & Update private instance attributes,
        but it only works with instance data and always behaves as instance method."""
        return self.__capsule_instance

    @instance_property.setter
    def instance_property(self, value):
        self.__capsule_instance = value

    @instance_property.deleter
    def instance_property(self):
        del self.__capsule_instance

    @classmethod
    def set_class_attribute(cls, value):
        cls.__capsule_class = value

    @classmethod
    def get_class_attribute(cls):
        return cls.__capsule_class

    @classmethod
    def del_class_attribute(cls):
        del cls.__capsule_class


if __name__ == "__main__":
    obj = Capsule()
    # obj.__capsule_instance  # AttributeError
    print(obj._Capsule__capsule_instance)  # Access Modifier
    print(Capsule._protected)
    print(Capsule.public)
