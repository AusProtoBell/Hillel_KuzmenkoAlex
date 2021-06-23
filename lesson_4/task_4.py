def output_num_stairs(n):
    new_list = []
    for i in range(1, n+1):
        new_list.append(i)
        str1 = ''.join(str(e) for e in new_list)
        print(str1)

n = int(input("Введите натуральное n<=9: "))
output_num_stairs(n)