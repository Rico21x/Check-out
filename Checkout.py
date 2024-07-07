class Checkout:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception(f"Item '{item}' does not have a price set to it!")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if count >= discount.nbrItems:
                    total += (count // discount.nbrItems) * discount.price
                    total += (count % discount.nbrItems) * self.prices[item]
                else:
                    total += count * self.prices[item]
            else:
                total += count * self.prices[item]
        return total
