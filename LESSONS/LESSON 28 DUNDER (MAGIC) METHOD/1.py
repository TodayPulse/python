# Write a __str__ method for a Cup class that returns "Small Cup" when the cup's size is "small"


class Cup:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        size_str = str(self.size)
        return f"{size_str.capitalize()} Cup"


print(Cup("small"))  
print(Cup(20))       