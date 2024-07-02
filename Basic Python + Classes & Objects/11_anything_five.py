"""
Python Exercise: anything five
function that take two integer parameter returns True if,
any value is 5, sum of value is 5 difference of value is 5
"""


def anything_five(num1: int, num2: int) -> bool:
    """
    anything five: check numbers is five difference is five sum is five, else
    @return False
    """
    if (
        abs(num1) == 5
        or abs(num2) == 5
        or abs(num1 - num2) == 5
        or abs(num2 - num1) == 5
        or abs(num1 + num2) == 5
    ):
        return True
    return False


if __name__ == "__main__":
    print(anything_five(5, 9))
    print(anything_five(5, 5))
    print(anything_five(6, 1))
    print(anything_five(6, 0))
    print(anything_five(100, 95))
