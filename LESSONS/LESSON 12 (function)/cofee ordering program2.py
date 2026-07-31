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


def menu_display():
    print("Available drink: Fanta")
    print("AVailable Quantity: 10")
    print("Price per cup: $4.50")


def cal(quantity,price):
    return quantity*price

def print_reciept(drink,quantity,price,total):
    print(f"------Coffee Receipt -------\nDrink: {drink}\nQuantity: {quantity}\nPrice per cup: ${price}\nTotal: ${total}")


def main():
    menu_display()

    drink= input ("WHat drink do you want?")
    quantity = int(input("What quantiy?"))
    price = float(input("Enter price per cup"))

    total = cal(quantity,price)

    print()

    print_reciept(drink,quantity,price,total)

if __name__ == "__main__":
    main()
    


    


