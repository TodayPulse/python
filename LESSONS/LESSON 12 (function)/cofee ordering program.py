# Build a simple coffee ordering program using functions:

# Create a function to display the menu.
# Create a function to calculate the total price.
# Create a function to print the receipt.
# Ask the user for:
# Drink name
# Quantity
# Price per cup
# Display a receipt similar to:
# ------ Coffee Receipt ------
# Drink: Latte
# Quantity: 3
# Price per Cup: $4.50
# Total: $13.50

def print_reciept():

    print('''Available Drink: Fanta
            Quantity available: 10
            Price per cup: $4.50''' )

    drink_name = input ("WHat drink do you want?")
    quantity = int(input("What quantiy?"))
    price = float(input("Enter price per cup"))

    total = quantity * price

    print(f"------Coffee Receipt -------\nDrink: {drink_name}\nQuantity: {quantity}\nTotal: ${total}")


print_reciept()
    


