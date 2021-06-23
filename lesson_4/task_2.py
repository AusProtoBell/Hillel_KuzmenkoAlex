def list_input():
    print("""Введите последовательность целых, неотрицательных чисел.
Введите 0 чтоб закончить ввод.""")
    count = 0
    mass = []
    num = 5
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            mass.append(num)
            count += 1
    return mass


def list_amount(mass):
    return len(mass)


def list_sum(mass):
    return sum(mass)


def list_comp(mass):
    comp = 1
    for i in mass:
        comp *= i
    return comp


def list_aver(mass):
    sum = 0
    for i in mass:
        sum += i
    return sum / len(mass)


def list_max_elem(mass):
    i = len(mass) - 1
    max_element = mass[i]
    max_index = i
    while i >= 0:
        if mass[i] >= max_element:
            max_element = mass[i]
            max_index = i
        i -= 1
    return [max_element, max_index+1]


def list_even_odd(mass):
    odd_amount = 0
    even_amount = 0
    for element in mass:
        if element % 2 == 0:
            even_amount += 1
        else:
            odd_amount += 1
    return [even_amount, odd_amount]


def second_max_element(mass):
    a = mass.copy()
    a.sort()
    a.reverse()
    max = a[0]
    req_elem = 0
    for i in a:
        if i < max:
            req_elem = i
            break
    return req_elem


def list_sum_max_elem(mass):
    sum_max = 0
    max_elem = 0
    for i in mass:
        if max_elem < i:
            max_elem = i
    for i in mass:
        if i == max_elem:
            sum_max += 1
    return sum_max


new_list = list_input()

print("Количество введённых чисел: ", list_amount(new_list))
print("Сумма: ", list_sum(new_list))
print("Произведение: ", list_comp(new_list))
print("Среднее арифметическое: ", list_aver(new_list))
print("Значение и порядковый номер наибольшего элемента: ", list_max_elem(new_list))
print("Количество чётных и нечётных элементов: ", list_even_odd(new_list))
print("Значение второго по величине элемента: ", second_max_element(new_list))
print("Количество повторение наибольшего элемента: ", list_sum_max_elem(new_list))
