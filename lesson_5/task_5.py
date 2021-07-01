def square_calc(side):
    perimeter = round(side * 4, 3)
    area = round(side ** 2, 3)
    diagonal = round((2**0.5) * side, 3)
    return perimeter, area, diagonal


req_side = float(input("Input size of your square: "))
rezult_list = list(square_calc(req_side))

print("""Perimeter = {0}
Area = {1}
diagonal = {2}""".format(rezult_list[0], rezult_list[1], rezult_list[2]))





