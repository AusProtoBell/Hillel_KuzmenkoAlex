import datetime


def is_date(day, month, year):
    try:
        data = datetime.date(year, month, day)
        return True
    except:
        return False


req_day = int(input("Day: "))
req_month = int(input("Month: "))
req_year = int(input("Year: "))

print(is_date(req_day, req_month, req_year))
