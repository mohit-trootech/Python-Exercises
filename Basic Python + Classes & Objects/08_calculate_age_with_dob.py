"""
Python Exercise to find the age of Person in Years using Date of Birth
"""

import datetime


class Person:
    """
    Person Class
    """

    now = datetime.date.today()

    def __init__(self, name: str, dob: str, country: str) -> None:
        """
        person class constructor
        """
        self.name = name
        self.dob = dob
        self.country = country

    def get_age(self) -> str:
        """
        method to get age
        """
        age_now = Person.now - self.dob
        age_now = age_now // datetime.timedelta(weeks=52)
        return "{} is Now {} Years Old Lives in {}".format(
            self.name, age_now, self.country
        )


n = input("Enter Your Name: ")
c = input("Enter the Country: ")
print("Enter Your Date of Birth: ")
y = input("Enter the Date of Year: ")
m = input("Enter the Date of Month 1-12: ")
d = input("Enter the Date of Day 1-31: ")
try:
    person_obj = Person(n, datetime.date(int(y), int(m), int(d)), c)
    print(person_obj.get_age())
except ValueError:
    print("Enter Date of Birth in Valid Number Format")
