def temp_calc(degree: float, temp_type: str):
    if temp_type == 'C':
        celsius = degree
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
    elif temp_type == 'K':
        kelvin = degree
        celsius = kelvin - 273.15
        fahrenheit = kelvin * 1.8 - 459.67
    elif temp_type == 'F':
        fahrenheit = degree
        celsius = (fahrenheit - 32) / 1.8
        kelvin = (fahrenheit + 459.67) / 1.8
    else:
        print("404 \nБыть может в следующих обновлениях придумают такой тип температуры. \nПопробуйте С, F или К")
        exit()
    return celsius, kelvin, fahrenheit


if __name__ == "__main__":
    user_degree = float(input("Сколько градусов? "))
    user_degree_type = input("С - Цельсий, K - Кельвин, F - Фаренгейт \nПо какой шкале? ").upper()

    print("C = {0}° \nK = {1}° \nF = {2}°".format(temp_calc(user_degree, user_degree_type)[0],
                                                  temp_calc(user_degree, user_degree_type)[1],
                                                  temp_calc(user_degree, user_degree_type)[2]))
