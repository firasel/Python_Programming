class Item:
    all = []

    def __init__(self, itemName, itemPrice) -> None:
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.all.append(self)

    def __repr__(self) -> str:
        return f'Item({self.itemName}, {self.itemPrice})'


item1 = Item("Mobile1", 150)
item2 = Item("Mobile2", 200)

item1.discount = 20

print(item1.__dict__)
print(item2.__dict__)
print(Item.all)
