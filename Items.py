

# after 30 seconds You earn 10 golds
class Hotel:
    def __init__(self, quantity, gold):
        self.gold = 0
        self.quantity = 0

    def hotel_buy(self, gold):
        if gold >= 20:
            print("Hotel has been bought")
        else:
            print("Not enough money to buy hotel")

class Motel:
    def __init__(self, quantity, gold):
        self.gold = 0
        self.quantity = 0

    def motel_buy(self, gold):
        if gold >= 1000:
            print("Motel has been bought")
        else:
            print("Not enough money to buy motel")

class House:
    def __init__(self, quantity, gold):
        self.gold = 0
        self.quantity = 0

    def house_buy(self, gold):
        if gold >= 100000:
            print("House has been bought")
        else:
            print("Not enough money to buy house")


