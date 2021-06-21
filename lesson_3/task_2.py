req_float_num = float(input("Input decimal fractional number: "))

fract_part = req_float_num % 1

count = 0
while count < len(str(req_float_num).split('.')[1]):
    fract_part *= 10
    count += 1

fract_part = int(fract_part)
first_fract = int(req_float_num * 10) % 10

print("Fractional part:", fract_part)
print("First digit after dot:", first_fract)
