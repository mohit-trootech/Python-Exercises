"""
Program that accepts an integer (n) and computes the value of (n+nn+nnn)
"""


def sum_pattern(num: int, pattern_length: str | int) -> int | None:
    """
    function to find the sum of pattern [n + nn + nnn]
    """
    try:
        result = []
        for size in range(1, int(pattern_length) + 1):
            result.append(int(num**size))
        print(result)
    except (ValueError, TypeError):
        print("Enter a Valid Number Input")


if __name__ == "__main__":
    # Drive Code
    sum_pattern(10, 4)
