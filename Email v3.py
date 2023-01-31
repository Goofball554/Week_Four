email = input("Please enter an email: ")

def checkLength(email):
    if len(email) > 10 and len(email) < 20:
        return True
    else:
        return False

def check_char(email):
    if "@" in email:
        return True
    else:
        return False

print(checkLength(email) and check_char(email))