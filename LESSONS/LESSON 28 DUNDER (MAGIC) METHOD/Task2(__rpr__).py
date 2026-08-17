# Create a Coin class with an attribute value_cents. 
# Implement __repr__ so that printing a list of coins shows something 
# like [Coin(25), Coin(10), Coin(5)].

class Coin:
    def __init__(self, value_cents):
        self.value_cents = value_cents

    def __repr__(self):
        return f"Coin({self.value_cents})"

coins = [Coin(25), Coin(10), Coin(5)]
print(coins)