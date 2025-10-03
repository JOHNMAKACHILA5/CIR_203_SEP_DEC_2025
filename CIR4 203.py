# 1. Create a dictionary with 5 products and their stock quantities
inventory = {
    "Laptop": 15,
    "Smartphone": 8,
    "Headphones": 25,
    "Keyboard": 12,
    "Mouse": 5
}

# 2. Add a new product and update the quantity of an existing one
inventory["Tablet"] = 10               # Adding new product
inventory["Smartphone"] = 18          # Updating existing product quantity

# 3. Function to return products with stock less than 10
def low_stock_items(inv):
    return [product for product, qty in inv.items() if qty < 10]

# 4. Delete a discontinued product and display updated dictionary
del inventory["Mouse"]                # Removing discontinued product
print("Updated Inventory:", inventory)

# 5. Use .items() to loop through and print each product with its quantity
print("\nProduct List:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
