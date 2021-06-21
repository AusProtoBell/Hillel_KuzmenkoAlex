list_of_six = range(100, 200, 6)

count = 0
while count < len(list_of_six):
    if list_of_six[count] % 5 == 0 and list_of_six[count] < 150:
        print(list_of_six[count])
    count += 1
