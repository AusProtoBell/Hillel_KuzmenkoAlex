exp_num = int(input("Input multivalued integer: "))
count_int = exp_num
rezult = 0

while count_int > 0:
    rezult += count_int % 10
    count_int = count_int // 10

print("Sum of all digits:", rezult)
