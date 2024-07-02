"""
Python Program to convert Integer Value to Roman
"""

symbols = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def integer_2_roman_numeral(num: int) -> str:
    """
    function to convert integer value to roman value
    """
    if isinstance(num, int):
        num = int(num)
        roman_numeral = ""
        while True:
            for i, j in symbols.items():
                if i <= int(num):
                    roman_numeral = roman_numeral + j
                    num -= i
                    break
            if num == 0:
                break

        return roman_numeral


if __name__ == "__main__":
    print(integer_2_roman_numeral(555))
