import csv
import re


def validity_number(auto_number: str):
    """Отловим все английские буквы, схожие внешне на украинские.
    Быть может есть более грамотное (питонячее) решение проблемы
    Но это всего две маленькие строчки, и самое важное - оно работает"""

    maket = ''.maketrans('ABEIKMHOPCTYX', 'АВЕІКМНОРСТУХ')
    auto_number = auto_number.upper().translate(maket)

    check = re.search(r'([А-Я]{2})(\d{4})([А-Я]{2})', auto_number)
    if not check:
        raise Exception("Не является автомобильным номером по украинским стандартам.")
    return check[1]


def get_csv_data():
    with open('ua_auto.csv', mode='r', encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        return list(data)


def region_name(auto_number, data):
    region = validity_number(auto_number)
    for row in data:
        if row['Код 2004'] == region or row['Код 2013'] == region:
            return f"Этот автомобиль зарегестирован в {row['Регіон']}"
    return "Очень похоже на украинский номерной знак, но такого региона нет"


if __name__ == '__main__':
    toyota = "BH2112СТ"
    csv_data = get_csv_data()
    print(region_name(toyota, csv_data))

    # get_region_name(a)
    # data = get_csv_data()
    # for row in data:
    #     print(row)
