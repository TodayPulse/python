# Task 3 — Custom Coffee Order
# Create a function called:

# make_drink(drink, milk, sugar)
# Requirements:

# Use parameters.
# Return a descriptive string.
# If sugar is greater than 0, include the sugar amount.
# Otherwise, don't mention sugar.
# Example:

# print(make_drink("Latte", "Almond", 2))
# print(make_drink("Espresso", "None", 0))
# Expected Output:

# Latte with Almond milk and 2 sugar packets
# Espresso with None milk


def make_drink(drink, milk, sugar):

    if sugar <= 0:
        sugar = ""
    else:
        sugar = f"and {sugar} sugar packets"

    return f"{drink} with {milk} milk {sugar}"


print(make_drink("Latte", "Almond", 2))
print(make_drink("Espresso", "None", 0))