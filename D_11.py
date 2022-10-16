class Phone:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def details(self):
        return f'Brand: {self.brand}\nColor: {self.color}\nPrice: {self.price}'


my_phone = Phone("Samsung", "Blue", 25000)
my_phone2 = Phone("Vivo", "Red", 20000)

print(my_phone.details())
print()
print(my_phone2.details())
