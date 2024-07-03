"""
In Python OOPs We have a setter getter and deleter method to get set and del a attribute.
"""


class Sample:
    """sample class to understand the getter setter and deleter"""

    def __init__(self):
        """sample constructor to create a self.value = None"""
        self.__value = None  # Access Specified: Private Attribute

    @property
    def sample_method(self):
        """to create a method a property add @property decorator in it.
        when we add property decorator it by default become a getter method.
        the main purpose of this is to protect the access specifiers"""
        return self.__value

    @sample_method.setter
    def sample_method(self, value):
        """@method_name.setter is used to set the attribute value"""
        self.__value = value

    @sample_method.deleter
    def sample_method(self):
        """@method_name.deleter is used to delete the attribute value
        del object.method_name is used to delete sample value"""
        del self.__value


if __name__ == "__main__":
    obj = Sample()
    print(obj, obj.__class__)
    obj.sample_method = "Set Value"
    print(obj.sample_method)
    del obj.sample_method
    try:
        print(obj.sample_method)
    except AttributeError:
        print("AttributeError")
    print(obj.__value)
