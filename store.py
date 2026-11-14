import products
from products import Product


class Store:

    # Intitialization
    def __init__(self, products: list[Product]):
        self.products = products

    # Methods
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products combined in the store."""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Returns a list of all products where is_active() is True."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Takes a list of tuples in the format (Product, quantity).
        Buys each product, updates inventory, and returns the total order price.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return float(total_price)
