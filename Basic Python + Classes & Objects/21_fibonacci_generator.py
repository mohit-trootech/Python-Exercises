"""
Program to Generator Fibonacci_Series to n Using Generator
"""


def fib_generator():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


if __name__ == "__main__":
    obj = fib_generator()
    for counter in range(15):
        print(next(obj), end=" - ")
