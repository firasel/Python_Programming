# inheritance
class Device:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def __repr__(self) -> str:
        return f'{self.brand} : {self.price} : {self.color}'


class Laptop(Device):
    def __init__(self, brand, price, color, disc_size) -> None:
        super().__init__(brand, price, color)
        self.disc_size = disc_size

    def run(self):
        print("Running the laptop")


class Phone(Device):
    def __init__(self, brand, price, color, camera, sim_number) -> None:
        super().__init__(brand, price, color)
        self.camera = camera
        self.sim_number = sim_number

    def run(self):
        print("Running the phone")


lenovo = Laptop("Lenovo", 35600, "Silver", "500gb")
hp = Laptop("Hp", 45000, "Black", "256gb")

print(lenovo)
print(hp)

samsung = Phone("Samsung", 20000, "Black", "10mp", 2)
iphone = Phone("IPhone", 150000, "Silver", "40mp", 1)
print(samsung)
print(iphone)

lenovo.run()
samsung.run()
