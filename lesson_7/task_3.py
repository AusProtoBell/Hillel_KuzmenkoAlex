import requests
import datetime


API_KEY = "f9ada9efec6a3934dad5f30068fdcbb8"
temp_day = []
temp_night = []
temp_feels_like = []
date = []


def input_user_request():
    city = input("Input name of Your city: ")
    days_num = input("Input quantity od days: ")
    return city, days_num


def send_request(city, days_num):
    return requests.get("http://api.openweathermap.org/data/2.5/forecast/daily",
                        params={'q': city, "cnt": days_num, "units": "metric", "appid": API_KEY}).json()


def get_filename(city, days_num):
    return "{0}_{1}_{2}_days_weather_forecast".format(date[0], city, days_num)


def write_to(filename, days_num):
    with open(f"{filename}.txt", 'w') as file:
        file.write("Date".ljust(20) + "Day temperature".ljust(20) + "Feels like".ljust(20) + "Night temperature".ljust(
            20) + "\n")
        for i in range(int(days_num)):
            file.write(date[i].ljust(20) + temp_day[i].ljust(20) + temp_feels_like[i].ljust(20) + temp_night[i] + "\n")


def data_computations(data):
    for day in data["list"]:
        temp_day.append(str(day["temp"]["day"]))
        temp_night.append(str(day["temp"]["night"]))
        temp_feels_like.append(str(day["feels_like"]["day"]))
        date.append(datetime.datetime.fromtimestamp(day["dt"]).strftime("%d-%m-%Y"))


def main():
    city, days_num = input_user_request()
    data = send_request(city, days_num)
    data_computations(data)
    filename = get_filename(city, days_num)
    write_to(filename, days_num)


main()


