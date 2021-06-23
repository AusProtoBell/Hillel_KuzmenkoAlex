def output(a, b):
    for i in range(a, b+1, 1):
        print(i, " ", end="")


def output_reverse(a, b):
    for i in range(a, b-1, -1):
        print(i, " ", end="")


first = int(input("Введите первое число (А): "))
second = int(input("Введите второе число (B): "))

if first < second:
    output(first, second)
else:
    output_reverse(first, second)
