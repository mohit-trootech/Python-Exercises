"""
Python Exercise to Find Arithmetic & Geometric Progression
"""


def arithmetic_progression(start: int, end: int, difference: int) -> tuple:
    """
    function to generate arithmetic progression
    """
    if isinstance(start, int) and isinstance(end, int) and isinstance(difference, int):
        return tuple(i for i in range(start, end + 1, difference))


def geometric_progression(start: int, end: int, ratio: int) -> tuple:
    """
    function to generate geometric progression
    """
    if isinstance(start, int) and isinstance(end, int) and isinstance(ratio, int):
        return tuple(start * ratio**i for i in range(0, end + 1))


if __name__ == "__main__":
    print("Arithmetic Progression: ", arithmetic_progression(1, 100, 5))
    print("Geometric Progression: ", geometric_progression(1, 10, 2))
