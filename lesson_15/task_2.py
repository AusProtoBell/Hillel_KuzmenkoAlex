import re


def format_number(phone_number: str):
    phone_number = re.sub(r'[^\d]', '', phone_number)
    phone_number = re.sub(r'(?:38)?(\d{3})(\d{3})(\d{2})(\d{2})',
                          r'(+38) \1 \2-\3-\4', phone_number)
    return phone_number


if __name__ == "__main__":
    print(format_number('063-999-99-99'))
    print(format_number('063 999-99-99'))
    print(format_number('063-99999-99'))
    print(format_number('+3806399-999-99'))
    print(format_number('380639999999'))
