"""
Python Exercise to find if string palindrome
"""


def is_palindrome(string):
    if string == "".join(list(reversed(string))):
        return True
    return False


if __name__ == "__main__":
    print(is_palindrome("maamaam"))
