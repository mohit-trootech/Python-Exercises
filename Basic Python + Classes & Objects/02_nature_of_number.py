"""
Python Exercise to Find the Nature of Number, Whether the Number is Positive, Negative, Zero
"""

try:
    num = float(input("Enter the Number: "))
    if num > 0:
        print("Number is Positive, {num}".format(num=num))
    elif num < 0:
        print("Number is Negative, {num}".format(num=num))
    if num == 0:
        print("Zero, {num}".format(num=num))
except ValueError:
    print("Please Enter a valid number input")
