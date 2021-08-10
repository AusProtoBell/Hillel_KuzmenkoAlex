from uuid import uuid4
import datetime


class UaBank:
    def __init__(self, bank_name: str, capital: float, commission: float):
        self.bank_name = bank_name
        self.capital = capital
        self.commission = commission

    def balance_check(self):
        return self.capital


class BankID:

    activity_list = []

    def __init__(self, user_name: str, balance: float):
        self.user_id = uuid4()
        self.user_name = user_name
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        self.activity_list.append([value, 'deposit', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def withdrawal_funds(self, value):
        if value> self.balance:
            raise Exception("Insufficient funds")
        self.balance -= value
        self.activity_list.append([f'-{value}', 'withdrawal', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def balance_check(self):
        return self.balance


def bank_transaction(user, bank, transaction_type, value):
    if transaction_type == 'deposit':
        user.deposit(value * (1 - bank.commission))
    elif transaction_type == 'withdrawal':
        user.withdrawal_funds(value * (1 + bank.commission))
    else:
        raise Exception('Incorrect transaction type')
    bank.capital += value * bank.commission


if __name__ == '__main__':

    user_one = BankID('Dave', 10000)
    bank_one = UaBank('SmileBank', 1000000, 0.01)

    bank_transaction(user_one, bank_one, 'deposit', 5000)
    bank_transaction(user_one, bank_one, 'withdrawal', 3500)

    print(user_one.user_id)
    print(user_one.balance_check())
    print(user_one.activity_list)
    print(bank_one.capital)
