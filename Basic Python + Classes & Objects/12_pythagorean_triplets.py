"""
Python Program to Check the Combination is Pythagorean Triples
"""

import math


def is_pythagorean_triples(triples: list) -> str | bool:
    if len(triples) == 3:
        triples = sorted(i**2 for i in triples)
        if sum(triples[:-1]) == triples[-1]:
            return True
        return False
    return "Please Enter 3 Triplets"


if __name__ == "__main__":
    print(is_pythagorean_triples([3, 5, 4]))
    print(is_pythagorean_triples([12, 15, 13]))
    print(is_pythagorean_triples([10, 12, 15]))
    print(is_pythagorean_triples([12, 5, 13]))
