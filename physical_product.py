# physical_product.py
# A PhysicalProduct IS-A Product, and it CAN BE shipped.

from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        # Reuse the Product constructor for the shared attributes
        super().__init__(product_id, name, price, stock)
        self.__weight = weight   # weight in kg

    def get_weight(self):
        return self.__weight

    # Overriding: show the parent's info first, then add the weight
    def display_information(self):
        super().display_information()
        print(f"    Type: Physical | Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product needs physical shipping."

    # Simple rule: $5 base fee + $2 for every kg
    def calculate_shipping_cost(self):
        return 5 + (2 * self.__weight)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
