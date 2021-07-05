def dict_construct(keys, values) -> dict:
    return dict(zip(keys, values))


cort_keys= (1, 2, 3, 4, 5)
cort_values = ("orange", "apple", "banana", "grapefruit", "watermelon")

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

fruits = dict_construct(cort_keys, cort_values)
crypto = dict_construct(coin, code)

print(fruits)
print(crypto)
