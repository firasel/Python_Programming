""" Manages Bank Account """


class Account:
    accID = 1

    def __init__(self, name, age, nid_num, balance) -> None:
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        # update acc id
        self.account_id = Account.accID
        Account.accID += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc_1 = Account('Rashed', 63, 61265, 500)
acc_2 = Account('Saidul', 23, 63254, 1000)

print(acc_1.account_id)
print(acc_2.account_id)

print(acc_1.balance)

acc_1.deposit(500)
print(acc_1.balance)

acc_1.withdraw(200)
print(acc_1.balance)
