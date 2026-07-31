# Task 2 — Customer Receipt Calculator
# Write a function called:

# calculate_total(quantity, price)
# The function should:

# Multiply the quantity by the price.
# Return the total cost.
# Example:

# total = calculate_total(4, 5.5)
# print(total)
# Expected Output:

# 22.0

def calculate_total(quantity, price):

    total = quantity * price

    return total

print(calculate_total(4,5.5))