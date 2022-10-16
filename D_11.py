class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'no money for you. Minimum withdraw: {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'you crossed max limit: {self.max_withdraw}'
        elif amount > self.balance:
            return 'You are broke!!! No money for you'
        else:
            self.balance = self.balance - amount
            return f'Here is your money: {amount}'


my_bank = Bank(20000)
print(my_bank.withdraw(1000))
print(my_bank.get_balance())
my_bank.deposit(2000)
print(my_bank.get_balance())
