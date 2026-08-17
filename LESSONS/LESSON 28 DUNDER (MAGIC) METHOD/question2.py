# (Master) Design an __add__ method for CardboardCup that allows cup_1 + cup_2 to 
# return a new CardboardCup object containing the combined liquid ounces of both cups. 
# What dunder method powers the + operator, and what would happen if you forgot to return 
# a new object and instead mutated self?


class CardboardCup:
    def __init__(self, size, drink, ounces):
        self.size = size
        self.drink = drink
        self.ounces = ounces

    # Correctly aligned with __init__ (inside the class, outside __init__)
    def __str__(self):
        return f"{self.size.capitalize()} {self.drink.capitalize()} Cup ({self.ounces} oz)"

    # Correctly aligned with __init__
    def __add__(self, other):
        if not isinstance(other, CardboardCup):
            return NotImplemented

        combined_ounces = self.ounces + other.ounces
        return CardboardCup(self.size, self.drink, combined_ounces)


cup_1 = CardboardCup("small", "fanta", 12)
cup_2 = CardboardCup("small", "fanta", 8)

cup_3 = cup_1 + cup_2
print(cup_3)  # Output: Small Fanta Cup (20 oz)