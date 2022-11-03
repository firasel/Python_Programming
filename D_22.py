class Item:
    def __init__(self, itemName, itemPrice) -> None:
        assert itemPrice >= 0 and itemPrice <= 10, f'Error line 3, {itemPrice} is invalid'
        self.itemName = itemName
        self.itemPrice = itemPrice

    def __repr__(self) -> str:
        return f"Name: {self.itemName}, Price: {self.itemPrice}"


item = Item("Car", 5)
print(item)
