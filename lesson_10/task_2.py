def hide_email(email: str):
    email = email.split('@')
    left_side = email[0]
    right_side = email[1]
    left_size = int(len(left_side)/2)
    right_size = int(len(right_side)/2)
    return f'{left_side[:left_size]}***@**{right_side[right_size:]}'


print(hide_email('somebody_email@gmail.com'))
