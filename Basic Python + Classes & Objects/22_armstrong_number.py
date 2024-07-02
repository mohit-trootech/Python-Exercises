"""
Python Program to Check String is Armstrong
example = 153: 1^3+5^3+3^3 == 153 and 1632: 1^4+6^4+3^4+2^4 == 1632
"""


def is_armstrong(num: str) -> bool | None:
    if isinstance(num, str):
        s = 0
        for i in num:
            s += int(i) ** len(num)
        if str(s) == str(num):
            return True
        else:
            return False
    print("Please Enter Valid Integer Input")


if __name__ == "__main__":
    print(is_armstrong("25"))
    print(is_armstrong("162"))
    print(is_armstrong("153"))
    print(is_armstrong("1634"))
