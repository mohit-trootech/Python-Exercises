"""
Python Exercise to Find LCM of Numbers
"""

from functools import reduce
import math


def lcm(*args):
    """python Program to find lcm"""
    return reduce(lambda a, b: a * b, args) // math.gcd(*args)


if __name__ == "__main__":
    print(lcm(20, 10, 30))
