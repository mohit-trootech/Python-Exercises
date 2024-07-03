"""As we see the types of attributes, please refer that first, we know that types of attributes are instance and class.
Similarly we have concept of types of method.
there are 3 types of method in a class: 1. Instance method 2. Class method 3. Static method"""


class Bank:
    """To understand the types of methods lets take an examples of bank.
    Bank have some class attribute that is bank specific not changes for each individual object that is
    ifsc_code, branch_name & bank_name. and also some instance attributes username, account_number etc.
    now lets understand the concept of types of methods with this awesome example.
    """

    ifsc_code = "ABC121212"
    branch_name = "ABC"
    bank_name = "XYZ Bank Pvt. Ltd."

    def __init__(self, username, account_number):
        """these are instance attributes for object"""
        self.username = username
        self.account_number = account_number

    def user_information(self):
        """this method is a instance method which is used to show user information.
        the thing about instance method is it takes self as parameter which indicates that the information
        required bu this method is object specific as no class can access this method"""
        print("User Information")
        print(self.username, self.account_number)
        print(self.bank_name, self.branch_name, self.ifsc_code)

    @classmethod
    def bank_information(cls):
        """this method is a class method which is used to show bank information.
        the things about class method is, it takes clas as parameter which indicates that the information
        required bu this method is class specific any class and any object same information from it.
        """
        print("Bank Information")
        print(cls.bank_name, cls.branch_name, cls.ifsc_code)

    @staticmethod
    def print_passbook():
        """this is a static method named print passbook. this is not a class method as well as not a instance method
        it is just a static method, because it neither takes self as argument, neither takes cls.
        the concept of static methods are utility they are created to increase utility.
        in this case user enter a bank enter passbook, and passbook gets print."""
        print("Passbook Printing")
        print("Printing Successfully")
        print("Collect Passbook")


if __name__ == "__main__":
    mohit = Bank("Mohit", 123456789)
    mohit.user_information()  # objects are used to access instance methods
    # objects are used to access class methods because object internally store Class Information
    mohit.bank_information()
    Bank.bank_information()  # classes are used to access class methods
    try:
        Bank.user_information()  # but when try to access instance methods with class throw TypeError
    except TypeError as te:
        print("TypeError", te)
    # static methods can be access by both a class and object
    mohit.print_passbook()
    Bank.print_passbook()
