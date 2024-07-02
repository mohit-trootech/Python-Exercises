import re


def repeat_pair(num):
    repeating_set = set()
    for i in str(num):
        if re.search(f"{i}.{i}", str(num)):
            repeating_set.add(int(i))
    if not repeating_set:
        return "No Repeat Pair"
    else:
        return "Alternating Number {}".format(repeating_set)


def check_postal(num):
    if 100000 <= num <= 999999:
        for i in str(num):
            if not re.findall(f"{i}.{i}", str(num)) == []:
                print("Invalid Postal Code")
                return repeat_pair(num)
        else:
            return "Postal Code is Valid"
    else:
        return "Out of Range"


try:
    postal_code = int(input("Enter Postal Code in Integer Format: "))
    print(check_postal(postal_code))
except ValueError:
    print("Try Entering a Number Input")
