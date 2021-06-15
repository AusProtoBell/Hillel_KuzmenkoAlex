print("""
sign(x) = 1,  если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0,  если x = 0.
""")

x = int(input("Input X: "))

if x > 0:
    print("sign(x) = 1")
elif x < 0:
    print("sign(x) = -1")
else:
    print("sign(x) = 0")
