"""Hierarchical Inheritance: In Hierarchical inheritance, more than one child class is derived from a single parent
class. In other words, we can say one base class and multiple derived classes."""


class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info("BMW")

obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")
