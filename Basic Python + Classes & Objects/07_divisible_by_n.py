"""
Program to Check if Number is Divisible by n
"""


def divisible(number: str | int, divisor: str | int) -> bool | None:
    """
    function to find the if the number is divisible by n
    """
    try:
        if int(number) % int(divisor) == 0:
            return True
        else:
            return False
    except ValueError:
        print("Please Enter a Valid Numeric Value")


if __name__ == "__main__":
    print(divisible(500, 10))
    print(divisible(500, 5))
    print(divisible(500, 25))
    print(divisible(500, 55))
    print(divisible.__annotations__)
