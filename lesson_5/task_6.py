def dict_cleaner(some_dict):
    new_dict = some_dict.copy()
    for key in some_dict:
        if some_dict[key] is None:
            del new_dict[key]
    return new_dict


dict_a = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(dict_a)

dict_a = dict_cleaner(dict_a)
print(dict_a)
