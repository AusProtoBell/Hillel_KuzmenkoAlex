import random
count = 3

while count>0:
    print("Attempts left:", count)
    user_num = int(input("Try your luck, input your number:"))
    random_num=random.randint(1,10)
    print("Random number is:", random_num)
    if random_num==user_num:
        print("YOU WIN!")
        exit()
    else:
        print("You lose(((")
    count-=1
