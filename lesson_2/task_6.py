some_list = list(range(10, 101, 10))
print("We have sequence of numbers: ", some_list)
x = float(input("Input X: "))

if abs(x) in some_list:
    print("X is contained in the sequence")
else:
    print("No, X is not contained in the sequence")
