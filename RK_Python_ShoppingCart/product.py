class Product:
    def __init__(self, product_name, product_cat, price, quantity):
        self.product_name = product_name
        self.product_cat = product_cat
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Name={self.product_name}, Category={self.product_cat}, Price={self.price}. Quantity={self.quantity}"
