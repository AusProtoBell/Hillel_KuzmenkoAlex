import random


class City:
    def __init__(self, street_count):
        self.streets = []
        self.initialize_city(street_count)

    def initialize_city(self, street_count):
        for street_id in range(street_count):
            self.streets.append(Street(street_id))

    def population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.humans
        return population

    def delete_street(self, street_id):
        self.streets.pop(street_id)

    def add_street(self):
        self.streets.append(Street(len(self.streets)))

    def population_report(self):
        with open('population-report.txt', mode='w', encoding='utf-8') as txt_file:
            txt_file.write(f'{"Улица".ljust(8)}{"Дом".ljust(8)}Население\n')
            for street in self.streets:
                for house in street.houses:
                    txt_file.write(f'{str(street.street_id).ljust(8)}{str(house.house_id).ljust(8)}{house.humans}\n')


class Street:

    min_houses_amount = 5
    max_houses_amount = 20

    def __init__(self, street_id):
        self.houses = []
        self.street_id = street_id
        for house_id in range(random.randint(self.min_houses_amount,
                                             self.max_houses_amount)):
            self.houses.append(House(house_id))

    def delete_house(self, street_id):
        self.houses.pop(street_id)

    def add_house(self):
        self.houses.append(House(len(self.houses) + 1))


class House:

    min_people_amount = 1
    max_people_amount = 100

    def __init__(self, house_id):
        self.house_id = house_id
        self.humans = random.randint(self.min_people_amount,
                                     self.max_people_amount)


if __name__ == '__main__':

    odessa = City(10)
    print(odessa.population())
    odessa.population_report()

