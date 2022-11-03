import json


class Item:
    all = []

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.all.append(self)

    def __repr__(self) -> str:
        return f'Item({self.name}, {self.price})'

    @staticmethod
    def initialize():
        with open('extract.txt', 'r') as file:
            data = file.read()
            js = json.loads(data)
        for item in js:
            Item(item['name'], item['price'])


Item.initialize()
print(Item.all)
