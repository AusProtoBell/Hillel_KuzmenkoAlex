from uuid import uuid4
import datetime


class BankID:

    bank_commission = 0.01
    # x% = x/100

    def __init__(self, user_name: str, balance: float):
        self.user_id = uuid4()
        self.user_name = user_name
        self.balance = balance
        self.activity_list = []

    def deposit(self, value):
        new_value = value * (1 - self.bank_commission)
        self.balance += new_value
        self.activity_list.append([new_value, 'deposit', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def withdrawal_funds(self, value):
        new_value = value * (1 + self.bank_commission)
        if new_value > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= new_value
        self.activity_list.append([f'-{new_value}', 'withdrawal', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def balance_check(self):
        return self.balance


if __name__ == '__main__':

    client_one = BankID("Dave", 10000)
    client_one.deposit(5000)
    client_one.withdrawal_funds(3500)

    print(client_one.balance_check())
    print(client_one.activity_list)
