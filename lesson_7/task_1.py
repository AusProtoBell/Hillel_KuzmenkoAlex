def as_list(func):
    def wrapper():
        new_list = func()
        return new_list.split()
    return wrapper


@as_list
def string_input():
    return input("Input some string: ")


print(string_input())

