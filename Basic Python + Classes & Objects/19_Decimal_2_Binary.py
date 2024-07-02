"""
Program to Covert any decimal number to binary Number
"""


def decimal2binary(decimal: int) -> str | None:
    """
    function to convert decimal to binary
    """
    try:
        binary = []
        while True:
            value = divmod(decimal, 2)
            binary += str(value[1])
            decimal = value[0]
            if decimal == 0 or decimal == 1:
                binary.append(str(decimal))
                break
        return "".join(sorted(binary, reverse=True))
    except (ValueError, TypeError):
        print("Please Enter Valid Number Input")
        return


if __name__ == "__main__":
    print(decimal2binary(7))
    print(decimal2binary(8))
    print(decimal2binary(11))
    print(decimal2binary(5))
    print(decimal2binary(14))
    print(decimal2binary(15))
