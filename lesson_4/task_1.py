def sport_tracker(x, y):
    days_count = 0
    while x <= finish:
        days_count += 1
        x *= 1.1
    return days_count


start = float(input("Спортсмен начал бегать в день по "))
finish = float(input("В итоге он начал бегать в день по "))

print("На это у него ушло", sport_tracker(start, finish), "дня(дней)")


