# inheritance
class Vehicle:
    def __init__(self, name, license, price) -> None:
        self.name = name
        self.license = license
        self.price = price
        print("Init called from Vehicle")

    def start(self):
        print(f'{self.name} started')


class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        print("Init called from Bus")
        super().__init__(name, license, price)
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price

    def sell_ticket(self, customer_name, quantity, amount):
        self.available_seats -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)
        return 'no ticket for you'


class Ticket:
    def __init__(self, owner) -> None:
        self.owner = owner


class AcBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        print("Init called from ACBus")
        super().__init__(name, license, price, seat, ticket_price)


city_bus = AcBus("CityBus", "JKP023", 2500000, 50, 500)
print(city_bus.__dict__)
