# Create a function that takes a list of items (as a list of strings). 
# Use a dictionary to store the price of these items. Calculate the total cost of the cart, 
# ignoring any items that are not in your price dictionary.

def calculate_cart_total(cart_items):
    # Dictionary storing the price of various items
    price_dictionary = {
        "apple": 1.50,
        "banana": 0.75,
        "milk": 2.20,
        "bread": 2.50,
        "eggs": 3.00,
        "cheese": 4.50,
        "rice": 5.00
    }
    
    total_cost = 0.00

    for item in cart_items:

        item_lower = item.lower()

        if item_lower in price_dictionary:
            total_cost += price_dictionary[item_lower]

    return total_cost

my_cart = ["Apple", "Milk", "UnknownItem", "Bread", "Banana"]
print(calculate_cart_total(my_cart))  # Output: 6.95


