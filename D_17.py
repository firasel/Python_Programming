class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.__balance = initial_balance

    def deposit(self, amount):
        print(f'Adding {amount} to your account')
        self.__balance += amount

    def withdraw(self, amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school):
        self.school = school
        super().__init__(holder, initial_balance)


rashid = StudentAccount('Rashid', 60000, 'DIU')
print(rashid.get_balance())
rashid.deposit(20000)
rashid.deposit(10000)
print(rashid.get_balance())
rashid.withdraw(5000)
print(rashid.get_balance())
