import random


def odd_elem(list):
    count = 0
    for index in range(len(list)):
        if list[index] % 2 != 0:
            count += 1
            list[index] = 0
    return count, list


some_list = []
for i in range(random.randint(5, 20)):
    some_list.append(random.randint(-100, 101))
print(some_list)

amount, some_list = odd_elem(some_list)
print("Amount of odd elements in list is:", amount)
print(some_list)
