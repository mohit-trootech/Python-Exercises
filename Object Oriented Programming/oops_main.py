"""Python is a multi-programming paradigm programming language. one of the most Popular approach is OOPs. OOPs is
based on Concepts of Classes & Objects which represents the real world blueprints and real world entity respectively.
Every Object has two characteristics: attributes & methods
The Concept of OOPs Allows Data Reusability
"""


class SampleClass:
    """
    class ClassName -> this allows us to implement a new Raw Class.
    this is sample document string for the class to give brief information about the classes &
    helpful for developers in understanding
    ClassName: class name always should be in CamelCase as it is Standard.
    """

    def __mohit__(self, value1):  # default __init__ changed to __mohit__ end of class
        """
        this is the sample __init__ constructor for the SampleClass.
        the use of constructor is to implement the assign the values for object when initialized
        __init__ constructor is passed with self argument with reference to the current object.
        """
        self.value1 = value1  # this is the sample attribute of object.
        self.value2 = None  # the attribute can be None by Default and setter method can be used to set the value later

    def sample_method(self):
        """
        this is the sample method related to that object.
        methods are just like the behaviour of any object.
        For Example: lets take a class for Car and a object bmw with is the object of that Car class,
        now the car must need attributes like brake, speed, mileage, etc.
        for method a bmw object also need behaviours like driving, acceleration, drifting etc
        MethodName: method name should follow snake_case as it is Standard.
        """
        print(self.value1)

    def sample_method_set_value_2(self, value):
        """
        each methods name is something like which explains the behaviour of the method.
        For Example: Current method is used to set the Value of object attribute self.value2
        needs to take self and the value as parameter
        similar method can be used to change the value of attributes
        """
        self.value2 = value

    __init__ = __mohit__  # this is the way you can change the constructor method name


sample_object = SampleClass("SampleValue")
print(sample_object)
print(sample_object.value1)
del sample_object  # a object is deleted using del keyword from existence
print(sample_object)
