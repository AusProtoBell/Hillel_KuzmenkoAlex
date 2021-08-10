from uuid import uuid4
import datetime


class BankID:

    activity_list = []

    def __init__(self, user_name: str, balance: float):
        self.user_id = uuid4()
        self.user_name = user_name
        self.balance = balance

    def deposit(self, value):
        self.balance += 0.99 * value
        self.activity_list.append([value, 'deposit', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def withdrawal_funds(self, value):
        if value * 1.01 > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= 1.01 * value
        self.activity_list.append([f'-{value}', 'withdrawal', datetime.datetime.now().strftime('%Y-%m-%d %I:%M%p')])

    def balance_check(self):
        return self.balance


if __name__ == '__main__':

    user_one = BankID('Dave', 10000)

    user_one.deposit(5000)
    user_one.withdrawal_funds(3500)

    print(user_one.user_id)
    print(user_one.balance_check())
    print(user_one.activity_list)
