def index_shift(some_string: str, index: int) -> str:
    index = index % len(some_string)
    return f'{some_string[-index:]}{some_string[:-index]}'


test_1 = '123456789'
test_2 = '123456789'

print(index_shift(test_1, 4))
print(index_shift(test_2, -4))
