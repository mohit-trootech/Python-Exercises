"""The process of inheriting the properties of the base (or parent) class into a derived (or child) class is called
inheritance. Inheritance enables us to define a class that takes all the functionality from a base class and allows
us to add more. In this tutorial, you will learn to use inheritance in Python.

The main purpose of Inheritance is Reusability of Code, as when we can inherit why to create from scratch
Type of Inheritance:
1. Single
2. Multiples
3. Multilevel
4. hierarchical
5. Hybrid
"""


class Vehicle:  # Parent class
    """this is the most basic example for single level inheritance as it require just a parent and a base class"""

    def __init__(self, sample_parent):
        print("Vehicle Class", sample_parent)


class Car(Vehicle):  # Child class
    """This is Child class inherits Vehicle class this means we can access attributes of child class with this.
    Now, what about constructor we are required to call constructor using super().__init__() method.
    similarly when we want to call the method with same name from child class super() method required.
    what about parameters, we can pass parameter also given in examples"""

    def __init__(self, sample_child, sample_parent):
        super(Car, self).__init__(sample_parent)
        print("Car class inherits Vehicle class", sample_child)


car = Car("Sample Child", "Sample Parent")

# Default issubclass() is built in method, returns true if class inherited any class
print(Car, Vehicle)
print(issubclass(Car, Vehicle))
print(issubclass(Vehicle, Car))
print(issubclass(Vehicle, object))
print(issubclass(Vehicle, list))

# Similarly, The built-in function isinstance() returns True if the object is an instance of the class or other classes
# derived from it. Each and every class in Python inherits from the base class object.
print("Is instance")
print(isinstance(car, Vehicle))
print(isinstance(car, Car))
print(isinstance(car, object))
print(isinstance(car, int))
print(isinstance(car, tuple))
