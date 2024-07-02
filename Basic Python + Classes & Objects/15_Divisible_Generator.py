"""
Generator Function to Find all the Number to Access Which are Divisible
"""


def divisible_generator(divisor):
    if isinstance(divisor, int):
        for i in range(1, divisor + 1):
            if divisor % i == 0:
                yield i
            i += 1
    else:
        print("Enter a Number Input")


if __name__ == "__main__":
    obj = divisible_generator(10)
    for j in obj:
        print(j)
