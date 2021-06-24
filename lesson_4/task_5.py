import random


def init_random_list(empty_x):
    new_list = []
    for i in range(20):
        new_list.append((random.randint(1, 10)))
    print(new_list)
    return new_list


def index_sym(some_list, i):
    print("Символ №{0} = {1}".format(i + 1, some_list[i]))


def pre_last(some_list):
    print("Предпоследний эелемент списка:", some_list[-2])


def first_five(some_list):
    print("Первые пять элементов списка:", some_list[:5])


def all_without_two_last(some_list):
    print("Все элементы без последних двух:", some_list[:-2])


def all_even_index(some_list):
    print("Все элементы с чётными индексами:", some_list[::+2])


def all_odd_index(some_list):
    print("Все элементы с нечётными индексами:", some_list[1::+2])


def reverse_symbols(some_list):
    print("Все элементы в обратном порядке:", some_list[::-1])


def reverse_cross(some_list):
    print("Элементы в обратном порядке через один:", some_list[::-2])


def length_list(some_list):
    print("Длина списка:", len(some_list))



req_list = []
req_list = init_random_list(req_list)

index_sym(req_list, 2)  # 1
pre_last(req_list)  # 2
first_five(req_list)  # 3
all_without_two_last(req_list)  # 4
all_even_index(req_list)  # 5
all_odd_index(req_list)  # 6
reverse_symbols(req_list)  # 7
reverse_cross(req_list)  # 8
length_list(req_list)  # 9
