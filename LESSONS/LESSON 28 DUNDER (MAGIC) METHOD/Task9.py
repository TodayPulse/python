# Create a Rectangle class with width and height. Implement:

# __str__ → "Rectangle(4 x 5)"
# __eq__ → two rectangles are equal if they have the same area, even if width/height differ
# (e.g. Rectangle(2, 6) == Rectangle(4, 3) should be True)
# __len__ → returns the integer perimeter (2 * (width + height))

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle {self.width} * {self.height}"

    def __eq__(self,others):
        if not isinstance(others,Rectangle):
            return False

        return self.width * self.height == others.width * others.height

    def __len__(self):
        return int (2 * (self.height + self.width))


r1 = Rectangle(4, 5)
r2 = Rectangle(2, 6)
r3 = Rectangle(4, 3)

print(r1)  # Output: Rectangle(4 x 5)
print(r2 == r3)  # Output: True (both have area 12)
print(len(r1))