"""Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that
is already provided by the parent class is provided by the child class. It is used to change the behavior of existing
methods and there is a need for at least two classes for method overriding. In method overriding, inheritance always
required as it is done between parent class(superclass) and child class(child class) methods."""


class TwoWheeler:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show(self):
        print("Details:", self.brand, self.model, "Price:", self.price)

    def gear_system(self):
        print("4 Gears are Available")

    def type_vehicle(self):
        print("Petrol or Diesel Based")


# inherit from vehicle class
class Bike(TwoWheeler):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)


class Scooter(TwoWheeler):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def gear_system(self):
        print("Scooter has Automatic Transmission")


class Electric(TwoWheeler):

    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def gear_system(self):
        print("Electric Vehicle has Automatic Transmission")

    def type_vehicle(self):
        print("Electric Type Vehicle")


splender = Bike("Honda", 2023, 40000)
print("Bike Info")
splender.show()
splender.type_vehicle()
splender.gear_system()
activa = Scooter("Honda", "2024 5G", 90000)
print("Scooter Info")
activa.show()
activa.type_vehicle()
activa.gear_system()
ather = Electric("Ather", 2020, 150000)
print("Electric Info")
ather.show()
ather.type_vehicle()
ather.gear_system()

# class A:
#     """method overriding is a example of run time polymorphism"""
#
#     def fun1(self):
#         print("feature_1 of class A")
#
#     def fun2(self):
#         print("feature_2 of class A")
#
#
# class B(A):
#     """Whereas in method overriding, inheritance always required."""
#
#     def fun1(self):
#         print("Modified feature_1 of class A by class B")
#
#     def fun3(self):
#         print("feature_3 of class B")
#
#
# # Create instance
# obj = B()
#
# # Call the override function
# obj.fun1()
