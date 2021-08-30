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
            pass

    def country_search(self, country=None):
        for line in self.csv_data:
            if line['iso_country'] == country.upper():
                self.airports.append(line)
        if not self.airports:
            pass

    def name_search(self, name=None):
        for line in self.csv_data:
            if name.lower() in line['name'].lower():
                self.airports.append(line)
        if not self.airports:
            pass

    @staticmethod
    def check_params(*arguments):
        if len([value for value in arguments if value is not None]) > 1:
            print(1)
            exit()
        if not len([value for  value in arguments if value is not None]):
            print(2)
            exit()

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
            raise IATACodeError



class IATACodeError(Exception):
    def __init__(self):



@click.command()
@click.option('--iata_code', '-i')
@click.option('--country', '-c')
@click.option('--name', '-n')
def main(iata_code, country, name):
    wow_airport = InquiryOfficeAirport(iata_code, country, name)
    print(wow_airport.get_search_result())


if __name__ == "__main__":
    main()

