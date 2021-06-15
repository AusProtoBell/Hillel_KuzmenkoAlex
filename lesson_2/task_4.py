year_num = int(input("Input verifiable year: "))
if year_num % 4 == 0 and (year_num % 100 != 0 or year_num % 400 == 0):
    print("YES")
else:
    print("NO")
