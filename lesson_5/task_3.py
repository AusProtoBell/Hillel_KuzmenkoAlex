def area_calc(h, a, x):
    if figure_type == "square":
        return h*a
    elif figure_type == "triangle":
        return h*a/2


figure_type = input("""Area of what figure are we looking for?
Print (triangle) or (square): """)
figure_type = figure_type.lower()

a = int(input("Input the length of the base: "))
h = int(input("input the length of the height: "))

print(area_calc(h, a, figure_type))
