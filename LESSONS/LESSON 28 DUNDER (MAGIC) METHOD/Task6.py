# Create a Temperature class storing a value in Celsius. Implement __len__ — even though 
# it's an unusual use — to return the integer part of the Celsius value (e.g. Temperature(21.7) → len(t) 
# returns 21). Explain in a comment why __len__ must never return a float or negative number.


class Temperature:
    def __init__(self, Celsius):
        self.Celsius = Celsius

    def __len__(self):
    # __len__ must never return a float because Python's len() protocol
    # strictly expects an integer (specifically, a non-negative integer).
    # Returning a float raises a TypeError, and returning a negative integer
    # raises a ValueError ("len() should return >= 0").
        return int(self.Celsius)


first = Temperature(21.7)

print(len(first))