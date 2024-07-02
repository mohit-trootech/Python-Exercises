"""
Python Exercise to Find the Simple Interest & Compound Interest
"""


class InterestCalculator:
    def __init__(self, principal: float, interest: float, time: float) -> None:
        self.principal = principal
        self.interest = interest
        self.time = time

    def calculate_simple_interest(self) -> int:
        """
        Python Program to Calculate Simple Interest
        @return: int
        """
        return round(
            self.principal + (self.principal * self.interest * self.time) / 100, 2
        )

    def calculate_compound_interest(self) -> int:
        """
        Python Program to Calculate Compound Interest
        @return: int
        """
        return round(
            self.principal * (1 + (self.interest / 100)) ** self.time - self.principal,
            2,
        )


if __name__ == "__main__":
    obj = InterestCalculator(5000, 5.5, 3)
    print(obj.calculate_simple_interest())
    print(obj.calculate_compound_interest())
