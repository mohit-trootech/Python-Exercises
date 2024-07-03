"""Duck typing is a type system where an object is considered compatible with a given type if it has all the methods
and attributes that the type requires. This type system supports the ability to use objects of independent and
decoupled classes in a specific context as long as they adhere to some common interface.

docs: A programming style which does not look at an object’s type to determine if it has the right interface;
instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck,
it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its
flexibility by allowing polymorphic substitution."""


class Duck:
    def swim(self):
        print("The duck is swimming")

    def fly(self):
        print("The duck is flying")


class Swan:
    def swim(self):
        print("The swan is swimming")

    def fly(self):
        print("The swan is flying")


class Albatross:
    def swim(self):
        print("The albatross is swimming")

    def fly(self):
        print("The albatross is flying")


if __name__ == "__main__":
    """lets Find our Duck"""
    birds = [Duck(), Swan(), Albatross()]
    for bird in birds:
        bird.fly()
        bird.swim()
