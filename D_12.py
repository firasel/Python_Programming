class Person:
    def __init__(self, name, age, money, height=26) -> None:
        self.name = name
        self.age = age
        self.money = money
        self.name = name
        self.height = height

    def __call__(self):
        return f'This is {self.name} with age {self.age} and have {self.money}'

    def __eq__(self, other) -> bool:
        return self.age == other.age

    def __len__(self):
        return self.height

    def __add__(self, other):
        return self.age + other.age


alim = Person('Alim', 15, 560, 35)
dalim = Person('Dalim', 16, 700)
print(alim+dalim)
# x = 5
# print(type(alim))
print(alim())
print("Compare two objects", alim == dalim)
print(len(alim))
