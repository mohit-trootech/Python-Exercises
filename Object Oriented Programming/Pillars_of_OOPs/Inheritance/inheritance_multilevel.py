"""In multilevel inheritance, we can also inherit from a derived class. It can be of any depth in Python.

All the features of the base class and the derived class are inherited into the new derived class.

For example, there are three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of
B. In other words, we can say a chain of classes is called multilevel inheritance."""


class Vehicle:  # Base class
    def Vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):  # derived class from Base 1
    def car_info(self):
        print("Inside Car class")


# Child class
class SportsCar(
    Car
):  # Derived class from derived class Car further derived from Vehicle
    def sports_car_info(self):
        print("Inside SportsCar class")


# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()


# Example 2:


class Animal:  # grandparent class
    def eat(self):
        print("Eating...")


class Dog(Animal):  # parent class
    def bark(self):
        print("Barking...")


class BabyDog(Dog):  # child class
    def weep(self):
        print("Weeping...")


d = BabyDog()
d.eat()
d.bark()
d.weep()
