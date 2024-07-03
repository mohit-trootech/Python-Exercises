"""In OOPs Python Attributes are the characteristics of the object.  as object required attributes for functionality
So, the attributes are linked to objects only? No Attributes are not only for object some attributes are class
related also, generally these are universal in nature. For Examples: Lets Say a Car class, so when we talk about a
car we know that 4 wheels in each car no matter what brand, just 4 wheels in car is universal.
so wheels for car is class attributes and other data like speed, mileage etc is object specific.
This concludes that there are two types of attributes in each class. 1. class attributes 2. instance attribute"""


class Car:
    """same Car class to explain types of attributes"""

    wheels = 4

    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage


if __name__ == "__main__":
    """Now lets create some objects for the class Car"""
    bmw = Car(
        120, 25
    )  # bmw object represents a real life car with speed 120 and mileage = 25
    audi = Car(
        100, 25
    )  # audi object represents a real life car with speed 100 and mileage = 25
    # now we can access the instance variables with object itself like
    print("BMW:", bmw.speed, bmw.mileage)
    print("Audi:", audi.speed, audi.mileage)
    # similarly object can also used to access class attributes
    print("BMW Wheels: ", bmw.wheels, "Audi Wheels: ", audi.wheels)
    # And class also used to access class attributes
    print("Car Wheels", Car.wheels)
    # some attributes are built in class attributes
    print(Car.__dict__)
    print(Car.__doc__)
    print(Car.__name__)
    print(Car.__module__)
    print(Car.__bases__)
    # But when we try to access instance attributes with class it throw Attribute Error
    try:
        print(Car.speed, Car.mileage)
    except AttributeError as e:
        print("AttributeError: ", e)
    # hope u understand the concepts of types of attributes
