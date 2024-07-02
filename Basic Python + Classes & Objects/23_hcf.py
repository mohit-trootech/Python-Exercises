"""
Python program to find the highest common factor
"""

from functools import reduce
from numpy import intersect1d as intersect


def is_prime(num):

    try:
        num = int(num)
        for i in range(2, num):
            if num == 1:
                print(f"{num} is Not Prime nor Composite")
                return False

            elif num == 2 or num == 3:
                return True
            elif num % i == 0:
                return False
        else:
            return True
    except ValueError:
        print("Enter a Numeric Integer Value")


def intersection_lists(*args):
    result_list = args[0]
    for i in range(1, len(args)):
        result_list = [i for i in args[i] if i in result_list]
    return sorted(result_list)


def hcf(*args):
    hcf_dict = {}
    for i in args:
        hcf_dict[i] = []
        if is_prime(i):
            hcf_dict[i].append(i)
        else:
            temp = i
            j = 2
            while j < temp:
                if i % j == 0:
                    i = int(i) // int(j)
                    hcf_dict[temp].append(j)
                else:
                    j += 1
    hcf_dict.setdefault("HCF", intersection_lists(*hcf_dict.values()))
    return hcf_dict


if __name__ == "__main__":
    print(hcf(24, 12, 6, 23))
