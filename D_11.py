class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def addToCart(self, item):
        self.cart.append(item)


shopper_1 = Shop("SS1")
shopper_1.addToCart("t-shirt")
print(shopper_1.cart)

shopper_2 = Shop("SS2")
shopper_2.addToCart("shoes")
print(shopper_2.cart)
