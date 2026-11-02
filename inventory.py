class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        for item in self.__products:
            if item.get_product_id() == product.get_product_id():
                print(f"Product ID '{product.get_product_id()}' already exists.")
                return False
        self.__products.append(product)
        return True

    def search_product(self, name):
        for item in self.__products:
            if item.get_name().lower() == name.lower():
                return item
        return None

    def display_all(self):
        if len(self.__products) == 0:
            print("The inventory is empty.")
            return
        for item in self.__products:
            item.display_information()

    def get_products_as_dicts(self):
        result = []
        for item in self.__products:
            result.append(item.to_dict())
        return result
