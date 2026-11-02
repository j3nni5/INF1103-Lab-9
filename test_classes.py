# test_classes.py
# Simple tests for section 7 of the lab. Run with: python test_classes.py

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

print("--- Test 1: Physical product shows weight ---")
guitar = PhysicalProduct("P100", "Guitar", 350.00, 5, 3.5)
guitar.display_information()

print("\n--- Test 2: Digital product shows download size ---")
game = DigitalProduct("D100", "Space Game", 29.90, 200, 1500)
game.display_information()

print("\n--- Test 3: get_fulfilment_info() ---")
print(guitar.get_fulfilment_info())
print(game.get_fulfilment_info())

print("\n--- Test 4: Product is abstract, so this should fail ---")
try:
    item = Product("X001", "Nothing", 1.00, 1)
    print("ERROR: a Product was created!")
except TypeError as error:
    print("Good! Cannot create a Product directly.")
    print("Python says:", error)

print("\n--- Test 5: Shipping cost for different weights ---")
light = PhysicalProduct("P101", "Pen", 2.00, 100, 0.1)
heavy = PhysicalProduct("P102", "Monitor", 300.00, 10, 8)
print(f"Pen (0.1 kg): ${light.calculate_shipping_cost():.2f}")
print(f"Monitor (8 kg): ${heavy.calculate_shipping_cost():.2f}")

print("\n--- Test 6: Digital product does not ship ---")
print("Is the digital product a CanBeShipped?", isinstance(game, CanBeShipped))
print("Is the physical product a CanBeShipped?", isinstance(guitar, CanBeShipped))
