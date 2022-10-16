class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def addToCart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        price = 0
        for item in self.cart:
            price += item['price'] * item['quantity']
        if amount < price:
            return f'Please give me more money: {price - amount}'
        if amount > price:
            return f'Here are the items and extra money: {amount - price}'
        else:
            return 'Here are the items'


shopping = Shopper('C1')
shopping.addToCart('shirt', 500, 4)
shopping.addToCart('shoes', 1450, 1)
shopping.addToCart('pant', 650, 1)

print(shopping.checkout(5000))
