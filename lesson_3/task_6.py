letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("""
Введите шахматный ход для вашего коня.
Важно! Вводите ход в формате настоящих шахмат!
Напрмер: A2 - D7
И не забудь верхний регистр и англ раскладку, ну будь ты человеком, а?

""")
start = input("Начальная точка фигуры: ")
finish = input("Конечная точка фигуры: ")
start = list(start)
finish = list(finish)
x1 = 0
x2 = 0
y1 = int(start[1])
y2 = int(finish[1])

for i in letter_list:
    a = int(letter_list.index(i))
    if start[0] == letter_list[a]:
        x1 = num_list[a]
    if finish[0] == letter_list[a]:
        x2 = num_list[a]


dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Да, конь может так ходить!')
else:
    print('Нет, конь не может так ходить!')
