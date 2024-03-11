import re


# function for validation of strong password
def StrongPasswordValidator(password):
    if len(password) < 8:
        message = "password should have atleast 8 char"
        return False, message
    if not re.search("[a-z]", password):
        message = "password should contain atleast one char from [a-z]"
        return False, message
    if not re.search("[A-Z]", password):
        message = "password should contain atleast one char from [A-Z]"
        return False, message
    if not re.search("[0-9]", password):
        message = "password should contain atleast one num from [0-9]"
        return False, message
    message = "Valid password"
    return True, message
