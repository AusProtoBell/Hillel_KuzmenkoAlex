import csv


class Product:
    # Класс продуктов. Объект ассортимента класса Store.
    # Ограничение на тип продукта. Только чай или кофе.
    def __init__(self, product_name, product_type, product_price):
        self.product_price = product_price
        self.product_name = product_name
        if product_type == 'tea' or product_type == 'coffee':
            self.product_type = product_type
        else:
            raise ValueError('Only coffee or tea type is allowed')

    def __str__(self):
        return f'{self.product_type}: {self.product_name}, цена: {self.product_price}грн.'

    def __repr__(self):
        return self.__str__()


class Store:
    # Класс кофейного магазина. Умеет загружать ассортимент от поставщика,
    # вернуть ассортимент по типу, вернуть стоимость всей продукции, продажа.
    def __init__(self):
        self.__assortment = []
        self.balance = 0

    def load_assortment(self, quantity=5):
        # Загрузка ассортимента из CSV фаила от поставщика.
        # Самому добавить объект для продажи не через поставщика нельзя
        # По умолчанию по пять штук каждой позиции.
        # Для нумерации каждого продукта отдельно стоит изменить накладную поставщика.
        # Загрузка ассоримента только выбранного типа (Чай и Кофе)
        # В цикле создаются объекты Product и заполняют лист.

        with open("inventory.csv", "r+", encoding="UTF-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['Тип'] == 'tea' or row['Тип'] == 'coffee':
                    for num in range(quantity):
                        self.__assortment.append(Product(row["Наименование"], row["Тип"], float(row["Цена"])))

    def check_assortment(self, product_type):
        # Ревизия ассортимента

        product_list = []
        for value in self.__assortment:
            if value.product_type == product_type or product_type == 'all':
                product_list.append(Product.__str__(value))
        if not product_list:
            raise Exception("Incorrect product type")
        return product_list

    def sell(self, name):
        # Продажа товара. Удаляем из ассортимента, стоимость на счёт магазина.

        check = True
        for index, value in enumerate(self.__assortment):
            if value.product_name == name:
                self.balance += value.product_price
                self.__assortment.pop(index)
                check = False
                break
        if check:
            raise Exception("Пардоньте, кончилось.")

    def warehouse_price(self):
        # Вернуть стоимость всех нераспроданных продуктов

        store_value = 0
        for value in self.__assortment:
            store_value += value.product_price
        return store_value


if __name__ == '__main__':

    wow_coffee = Store()
    wow_coffee.load_assortment()
    print(wow_coffee.check_assortment('coffee'))
    wow_coffee.sell("Эспрессо")
    print(wow_coffee.balance)
    print(wow_coffee.warehouse_price())
