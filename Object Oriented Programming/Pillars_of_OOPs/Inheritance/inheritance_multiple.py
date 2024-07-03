"""In multiple inheritance, one derived class can inherit from multiple base classes."""


class Person(object):  # Parent: 1
    """base class - 1, to represent the Person"""

    def __init__(self, name):
        super(Person, self).__init__()
        print("Inside Person class")
        print("Person, Name:", name)


class Company:  # Parent: 2
    """base class - 2, to represent the Company"""

    def __init__(self, company_name):
        print("Inside Company class")
        print("Company, Name:", company_name)


class Employee(Person, Company):  # Child Class
    """child class - derived from Person and Company"""

    def __init__(self, skill, name, company_name):
        super(Person, self).__init__(name)
        print("Inside Employee class")
        print("Employee, Skill:", skill)


if __name__ == "__main__":
    # emp = Employee("ML", "Mohit")
    emp = Employee("ML", "Mohit", "Trootech")
