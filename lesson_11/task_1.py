def user_input() -> list:
    user_txt = []
    print("Write your text below:")
    while True:
        user_txt.append(input())
        if user_txt[len(user_txt)-1] == '':
            break
    return user_txt


def write_to_txt():
    with open('test.txt', mode='w') as txt_file:
        text = user_input()
        for row in text:
            txt_file.write(f'{row}\n')


write_to_txt()
