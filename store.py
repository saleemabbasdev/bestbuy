import products
from products import Product


class Store:

    def __init__(self, products: list[Product]):
        self.products = products

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


def order(self, shopping_list: list[tuple]) -> float:
    """
    Takes a list of tuples in the format (Product, quantity).
    Buys each product, updates inventory, and returns the total order price.
    """
    total_price = 0.0
    for product, quantity in shopping_list:
        # Calls the product's buy method which handles stock validation and cost calculation
        total_price += product.buy(quantity)

    return float(total_price)


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
