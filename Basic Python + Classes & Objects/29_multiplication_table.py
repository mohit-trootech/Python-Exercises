"""
Python Program to create Multiplication Table
"""


def multiplication_table(num: int) -> None:
    """
    function to print multiplication Table
    """
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")


if __name__ == "__main__":
    multiplication_table(10)
