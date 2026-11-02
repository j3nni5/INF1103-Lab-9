import json
import os
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory

FILENAME = "inventory.json"


def load_inventory(inventory):
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            # The "type" tells us which class to create
            if item["type"] == "physical":
                product = PhysicalProduct(item["product_id"], item["name"],
                                          item["price"], item["stock"],
                                          item["weight"])
            elif item["type"] == "digital":
                product = DigitalProduct(item["product_id"], item["name"],
                                         item["price"], item["stock"],
                                         item["download_size"])
            else:
                print(f"Unknown product type: {item['type']}")
                continue
            inventory.add_product(product)
    else:
        # No file yet, so start with some default products
        inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 14, 2.5))
        inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.1))
        inventory.add_product(DigitalProduct("D001", "Photo Editor", 59.90, 100, 450))


def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory.get_products_as_dicts(), file, indent=4)


def show_menu():
    print("""
----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------""")


def add_new_product(inventory):
    print("Product type: 1. Physical   2. Digital")
    type_choice = input("Enter product type (1 or 2): ")
    if type_choice != "1" and type_choice != "2":
        print("Invalid product type.")
        return

    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        if type_choice == "1":
            weight = float(input("Enter weight in kg: "))
            product = PhysicalProduct(product_id, name, price, stock, weight)
        else:
            download_size = float(input("Enter download size in MB: "))
            product = DigitalProduct(product_id, name, price, stock, download_size)
    except ValueError:
        print("Invalid number. Product not added.")
        return

    if inventory.add_product(product):
        print(f"Product '{name}' added successfully.")


inventory = Inventory()
load_inventory(inventory)

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        add_new_product(inventory)

    elif choice == "3":
        name = input("Enter product name to update stock: ")
        product = inventory.search_product(name)
        if product is None:
            print(f"Product '{name}' not found in inventory.")
        else:
            try:
                new_stock = int(input("Enter new stock quantity: "))
            except ValueError:
                print("Invalid number. Stock not changed.")
                continue
            if product.update_stock(new_stock):
                print(f"Stock for '{name}' updated to {new_stock}.")

    elif choice == "4":
        name = input("Enter product name to search: ")
        product = inventory.search_product(name)
        if product is None:
            print(f"Product '{name}' not found in inventory.")
        else:
            product.display_information()
            print("    Fulfilment:", product.get_fulfilment_info())
            # Only products that CanBeShipped have a shipping cost
            if isinstance(product, CanBeShipped):
                print(f"    Shipping cost: ${product.calculate_shipping_cost():.2f}")

    elif choice == "5":
        save_inventory(inventory)
        print("Inventory saved successfully.")

    elif choice == "6":
        save_inventory(inventory)
        print("Exiting the program. Inventory saved.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
