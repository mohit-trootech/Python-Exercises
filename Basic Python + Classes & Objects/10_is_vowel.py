"""
Python Exercise to Return whether the Provided input is a Vowel or Not
"""


def is_vowel(letter: str) -> bool | None:
    vowels = ("a", "e", "i", "o", "u")
    if str(letter).lower() in vowels:
        return True
    return False


if __name__ == "__main__":
    print(is_vowel(4))
    print(is_vowel("444"))
    print(is_vowel("a"))
    print(is_vowel("u"))
    print(is_vowel("l"))
