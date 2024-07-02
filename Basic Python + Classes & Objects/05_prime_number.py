"""
Python Exercise to Find Prime Number
"""


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


if __name__ == "__main__":
    print(is_prime(7))
    print(is_prime(9))
    print(is_prime(8))
    print(is_prime(21))
    print(is_prime(2111))
