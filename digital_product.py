# digital_product.py
# A DigitalProduct IS-A Product. It does NOT use CanBeShipped.

from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        # Reuse the Product constructor for the shared attributes
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size   # size in MB

    def get_download_size(self):
        return self.__download_size

    # Overriding: show the parent's info first, then add the download size
    def display_information(self):
        super().display_information()
        print(f"    Type: Digital | Download size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally (download)."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data
