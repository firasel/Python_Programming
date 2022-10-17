class Shopping:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    @staticmethod
    def multiply(x, y):
        return x*y

    def add_to_cart(self, item, price, quantity):
        item_total = price * quantity
        self.total += item_total
        self.items.append(item)

    def checkout(self):
        pass


print(Shopping.multiply(10, 20))
