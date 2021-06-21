fact_num = int(input("Enter the number you are looking for factorial: "))

rezult = 1
count = 1

while count <= fact_num:
    rezult *= count
    count+=1

print("Factorial =", rezult)
