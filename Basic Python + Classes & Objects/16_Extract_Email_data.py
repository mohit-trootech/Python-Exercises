# Python Program to Extract Username & Email


def extract_username_domain(email):
    return {
        "username": email[: email.index("@")],
        "domain": email[email.index("@") :],
        "company": email[email.index("@") + 1 : email.index(".")],
    }


print(extract_username_domain("john@email.com"))
