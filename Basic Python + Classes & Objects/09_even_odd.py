"""
Program to Get Even Number list Till n
"""


def is_even(num: str | int) -> bool | None:
    try:
        if int(num) % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        print("Please Enter a Valid Number")
        return


if __name__ == "__main__":
    print(is_even(4))
    print(is_even(5))
    print(is_even(7))
    print(is_even(7314))
