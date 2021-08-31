# 1) функции аэропорта YES
# 2) условия работы аэопорта YES
# 3) классы ошибок
# 4) аргпарсер параметров YES
# 5) проверка ята_кода
import csv
import click
import re


class InquiryOfficeAirport:
    def __init__(self, iata_code=None, country=None, name=None):
        self.iata_code = iata_code
        self.country = country
        self.name = name
        self.airports = []
        self.check_params(iata_code, country, name)

    @property
    def csv_data(self):
        with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
            data = csv.DictReader(file, delimiter=',')
            return [line for line in data]

    def iata_code_search(self, iata_code=None):
        for line in self.csv_data:
            if line['iata_code'] == iata_code:
                self.airports.append(line)
        if not self.airports:
            raise AirportNotFoundError(iata_code, 'Airport not found')

    def country_search(self, country=None):
        for line in self.csv_data:
            if line['iso_country'] == country.upper():
                self.airports.append(line)
        if not self.airports:
            raise CountryNotFoundError(country, 'Country not found')

    def name_search(self, name=None):
        for line in self.csv_data:
            if name.lower() in line['name'].lower():
                self.airports.append(line)
        if not self.airports:
            raise AirportNotFoundError(name, 'Airport not found')

    @staticmethod
    def check_params(*arguments):
        qrgs_qty = len([value for value in arguments if value is not None])
        if qrgs_qty > 1:
            raise MultipleOptionsError(qrgs_qty, 'Обязателен и необходим лишь один параметр для поиска')
        if not qrgs_qty:
            raise NoOptionsError(qrgs_qty, 'Обязателен и необходим один параметр для поиска')

    def get_search_result(self):
        if self.iata_code:
            self.iata_code_check(self.iata_code)
            self.iata_code_search(self.iata_code)
        if self.country:
            self.country_search(self.country)
        if self.name:
            self.name_search(self.name)
        return self.airports

    @staticmethod
    def iata_code_check(iata_code):
        match = re.fullmatch(r'[A-Z]{3}', iata_code)
        if not match:
            raise IATACodeError(iata_code, 'IATA код может быть только 3х буквенным в верхнем регистре')


class IATACodeError(Exception):
    def __init__(self, data, message):
        self.message = message
        self.data = data

    def __str__(self):
        return f'("{self.message}", "{self.data}")'


class AirportNotFoundError(Exception):
    def __init__(self, data, message):
        self.message = message
        self.data = data

    def __str__(self):
        return f'{self.data} - {self.message}'


class CountryNotFoundError(Exception):
    def __init__(self, data, message):
        self.message = message
        self.data = data

    def __str__(self):
        return f'{self.data} - {self.message}'


class MultipleOptionsError(Exception):
    def __init__(self, data, message):
        self.message = message
        self.data = data

    def __str__(self):
        return f'("{self.message}", "{self.data}")'


class NoOptionsError(Exception):
    def __init__(self, data, message):
        self.message = message
        self.data = data

    def __str__(self):
        return f'("{self.message}", "{self.data}")'


@click.command()
@click.option('--iata_code', '-i')
@click.option('--country', '-c')
@click.option('--name', '-n')
def main(iata_code, country, name):
    wow_airport = InquiryOfficeAirport(iata_code, country, name)
    print(wow_airport.get_search_result())


if __name__ == "__main__":
    main()

