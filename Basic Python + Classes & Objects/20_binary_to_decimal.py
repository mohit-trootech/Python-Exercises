"""
Program to Covert any binary number to decimal Number
"""


def binary2decimal(binary):
    decimal = 0
    size_binary = len(binary) - 1
    if binary.isnumeric():
        for i in binary:
            decimal += int(i) * (2**size_binary)
            size_binary -= 1
        return decimal


if __name__ == "__main__":
    print(binary2decimal("1111"))
    print(binary2decimal("1110"))
    print(binary2decimal("1100"))
    print(binary2decimal("111"))
