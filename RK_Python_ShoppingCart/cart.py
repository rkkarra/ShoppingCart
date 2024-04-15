from product import Product


class Cart:
    def __init__(self):
        self.cart_items = list() # [[Product, cart_quant, Amount]

    def add(self, prod, cart_quant):
        self.cart_items.append([prod, cart_quant, self.calculate_amount(prod.price, cart_quant)])

    def update(self, prod_name, cart_quantity):
        for i in self.cart_items:
            if i[0].product_name == prod_name:
                i[1] = cart_quantity
                i[2] = self.calculate_amount(i[0].price, i[1])
                print(f"You have updated {i[0].product_name}, Cart Qty: {i[1]}, Amount: {i[2]} in your cart.")

    def remove(self, prod_name):
        for i in self.cart_items:
            if i[0].product_name == prod_name:
                self.cart_items.remove(i)
                print(f"You have removed {i[0].product_name}, Cart Qty: {i[1]}, Amount: {i[2]} from cart.")

    def view(self):
        if not self.cart_items:
            print("Your cart is empty! Shop around to add.")
        else:
            print("Cart")
            for i in self.cart_items:
                print(f"Product: {i[0].product_name}, Cart Qty: {i[1]}, Amount: {i[2]}")

    @staticmethod
    def calculate_amount(product_price, cart_quant):
        amount = product_price * cart_quant
        return amount

    def calculate_total(self):
        total = 0
        for i in self.cart_items:
            total += i[2]
        return total


# cart = Cart()
# product = Product("FWFBoots", "footwear", 99.99, 2)
#
# cart.add(product, 2)
# cart.view()
# cart.update("FWFBoots", 1)
# cart.view()
# cart.remove("FWFBoots")
# cart.view()
