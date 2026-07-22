# Data Cleaning: 
# Take a list of dictionaries representing product data. Some keys might be missing. 
# Write code to filter out any dictionaries that do not have both a 'name' and 'price' key.




def filter_valid_products(products):

    valid_product = []

    for product in products:
        if 'name' in product and 'price' in product:
            valid_product.append(product)

    return valid_product

# --- Example Usage ---
product_list = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Mouse"},  # Missing 'price'
    {"price": 19.99},    # Missing 'name'
    {"name": "Keyboard", "price": 49.99}
]

print(filter_valid_products(product_list))