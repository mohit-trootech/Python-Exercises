"""Abstraction is used to hide the internal functionality of the function from the users. The users only interact 
with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function 
does" but they don't know "how it does."""

from abc import ABC, abstractmethod  # Abstraction is Achieved Through inheritance


class RBI(ABC):
    """Lets understand Abstraction with a General Example. we have a class called RBI. now this RBI class inherits
    ABC so this is also abstract base class. Now each and Every Bank must inherit RBI rules and regulations,
    on of the rule is RTI. Now the question aries how to impose this to banks. Here, comes the role of abstract base
    classes. This allow RBI to enforce the RTI rule without this they are not Operational
    """

    @staticmethod
    @abstractmethod
    def rti():
        """rti method in abstract class comes with a decorator. the implementation of this method is not here.
        but the classes that inherits abstract base class impose to have a rti method.
        """
        pass


class SBI(RBI):

    @staticmethod
    def rti():
        return "RTI Rules are Available in SBI"


class PNB(RBI):

    @staticmethod
    def rti():
        return "RTI Rules are Available in PNB"


class AxisBank(RBI):
    """This Bank Don't Follow rti Method so No Authentication from RBI: TypeError"""


if __name__ == "__main__":
    sbi = SBI()
    print(sbi.rti())
    pnb = PNB()
    print(pnb.rti())
    ab = AxisBank()
