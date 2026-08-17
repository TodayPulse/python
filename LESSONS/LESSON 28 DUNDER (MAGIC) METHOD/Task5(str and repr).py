# Create a Backpack class that stores items in a list (self.items). 
# Implement both __str__ (a friendly summary like "Backpack with 3 items")
# and __repr__ (a technical form like Backpack(['pen', 'notebook', 'water bottle'])). 
# Test that print(my_backpack) and printing [my_backpack] show different outputs.


class Backpack:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f"Backpack with {len(self.items)} items"

    def __repr__(self):
        return f"Backpack({self.items!r})"


my_backpack = Backpack(['pen', 'notebook', 'water bottle'])

print(my_backpack)       # Output: Backpack with 3 items
print([my_backpack])     # Output: [Backpack(['pen', 'notebook', 'water bottle'])]