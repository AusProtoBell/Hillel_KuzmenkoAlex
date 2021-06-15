speed = int(input("What is Vasya's speed? "))
time = int(input("How long does Vasya rides? "))
if time < 0:
    print("Vasya obmanul vremya i prostranstvo? Ne mozhet byt' otricatel'noe vremya!")
    exit()

rez = speed * time

if 0 <= rez <= 100:
    print(rez)
elif 0 > rez >= -100:
    print(100 + rez)
else:
    print("VASYA, ASTANAVIS', TY UJE DALEKO UEHAL!!!")
