def dict_construct(some_list) -> dict:
    rez_dict = {}
    for i in range(len(some_list)):
        rez_dict[i] = some_list[i]
    return rez_dict


some_list = ['a', 'b', 'c', 'd', 'e']
some_values = ("orange", "apple", "banana", "grapefruit", "watermelon")


print(dict_construct(some_list))
print(dict_construct(some_values))
