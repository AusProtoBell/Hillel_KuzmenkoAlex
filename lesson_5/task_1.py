def is_prime(x):
    rez: bool = True
    for i in range(2, x):
        if x % i == 0:
            rez = False
    return rez


req_num: int = int(input("Input checked number: "))
print(is_prime(req_num))
