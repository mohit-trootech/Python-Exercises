"""
Python Program to Count Occurring Vowels and Consonants in User Input String
"""


def is_vowel(data: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    count = {"vowels": 0, "consonants": 0}
    words_list = [word for word in data.split(" ") if word != ""]
    for word in words_list:
        for char in word:
            if char in vowels:
                count["vowels"] += 1
            else:
                count["consonants"] += 1
    return count


if __name__ == "__main__":
    sentence = input("Enter Something: ")
    print(is_vowel(sentence))
