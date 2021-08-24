import re


def input_pass():
    return input("Input password: ")


def validated_pass():
    password = input_pass()
    if not re.search(r'[a-z]', password):
        print("Requires at least 1 lower case symbol")
        password = validated_pass()
    if not re.search(r'[A-Z]', password):
        print("Requires at least 1 upper case symbol")
        password = validated_pass()
    if not re.search(r'[0-9]', password):
        print("Requires at least 1 digit")
        password = validated_pass()
    if not re.search(r'[$#@\-+=]', password):
        print("Requires at least 1 special symbol")
        password = validated_pass()
    if not len(password) > 7:
        print("Requires at least 8 symbols")
        password = validated_pass()
    return password


true_password = validated_pass()
print('Password is correct')
