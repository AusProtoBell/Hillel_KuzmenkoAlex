import random


class City:
    # Класс Город. Содержит список улиц и функционал:
    # 1) Инициализировать город
    # 2) перепись населения
    # 3) удалить/добавить улицу/дом
    # 4) вывести в текстовый фаил данные по переписи населения

    def __init__(self):
        self.list_of_streets = []
        self.allowable_houses_amount = [5, 20]
        self.allowable_people_amount = [1, 100]

    def declare_city(self, num_of_streets):
        # Инициализируем город. Наполняем в цикле город улицы, а каждую улицу домами
        # в случайных количествах в рамках ограничений.

        for street_id in range(num_of_streets):
            self.list_of_streets.append(Street(street_id))
            for house_id in range(random.randint(5, 20)):
                self.list_of_streets[street_id].list_of_houses.append(House(house_id))
                self.list_of_streets[street_id].list_of_houses[house_id].humans = random.randint(1, 100)
        print("The city was generated")

    def population_census(self):
        # Перепись населения

        population = 0
        for street in self.list_of_streets:
            for house in street.list_of_houses:
                population += house.humans
        return population

    def delete_street(self, index):
        # Удалить улицу
        self.list_of_streets.pop(index)

    def add_street(self):
        # Добавить улицу
        self.list_of_streets.append(Street(self.list_of_streets.__len__()))

    def delete_house(self, street_id, house_id):
        # Удалить дом, если не нарушает закон о минимальном количестве домов на улицу

        if self.allowable_houses_amount[0] < self.list_of_streets[street_id].list_of_houses.__len__():
            self.list_of_streets[street_id].list_of_houses.pop(house_id)
        else:
            print("Слишком мало домов по правилам города")
            pass

    def add_house(self, street_id):
        # Добавить дом, если не нарушает закон о максимальном количестве домов на улицу

        if self.allowable_houses_amount[1] > self.list_of_streets[street_id].list_of_houses.__len__():
            self.list_of_streets[street_id].list_of_houses.\
                append(House(self.list_of_streets[street_id].list_of_houses.__len__()))
        else:
            print("Слишком много домов по правилам города")
            pass

    def population_report(self):
        # Запись в текстовый файл информацию по количеству людей в каждом доме на каждой улице

        with open('population-report.txt', mode='w', encoding='utf-8') as txt_file:
            txt_file.write('Улица'.ljust(8) + 'Дом'.ljust(8) + 'Население' + '\n')
            for street in self.list_of_streets:
                for house in street.list_of_houses:
                    txt_file.writelines(f'{str(street.street_id+1).ljust(8)}'
                                        f'{str(house.house_id+1).ljust(8)}'
                                        f'{house.humans}' + '\n')


class Street:
    # Объект Улица. Содержит список домов.

    def __init__(self, street_num):
        self.list_of_houses = []
        self.street_id = street_num


class House:
    # Объект Дом. Содержит количество проживающий людей.

    def __init__(self, house_num):
        self.humans = 0
        self.house_id = house_num


odessa = City()
odessa.declare_city(10)
print(odessa.population_census())
odessa.population_report()
