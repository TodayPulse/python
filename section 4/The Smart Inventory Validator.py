# Challenge 1: The Smart Inventory Validator (Functions, If-Else Shorthand, pass)
# Concepts Tested: Standard functions, conditional shorthand (ternary operators), and the pass placeholder.

# The Task: Write a function named validate_stock(item_name, stock_count) that:

# Uses a ternary conditional statement (if-else shorthand) to assign a status string: "Critical" 
# if stock is less than 5, otherwise "Healthy".

# If the item_name is explicitly equal to "DUMMY_ITEM", the function should do nothing yet and use 
# the pass statement to bypass execution cleanly, returning None.

# Otherwise, it should return a formatted string: f"Item: {item_name} | Status: {status}".

def validate_stock(item_name, stock_count):

    if item_name == "DUMMY_ITEM":
        pass

    else:
        status = "Critical" if stock_count < 5 else "Healthy"

        return f"Item: {item_name} ! Status: {status}"


# --- Example usage ---
print(validate_stock("Widget", 3))          # Item: Widget | Status: Critical
print(validate_stock("Gadget", 12))         # Item: Gadget | Status: Healthy
print(validate_stock("DUMMY_ITEM", 100))    # None