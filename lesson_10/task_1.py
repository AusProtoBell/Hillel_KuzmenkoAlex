def count_points():
    win, draw, loss = user_input()
    return (win * 3) + draw


def user_input() -> tuple:
    win = int(input("How many wins?: "))
    draw = int(input("How many draws?: "))
    loss = int(input("How many losses?: "))
    return win, draw, loss


print(f'Total amount of points: {count_points()}')
