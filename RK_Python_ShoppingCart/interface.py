from product import Product


class Interface:
    def __init__(self):
        self.products = {"clothing": [Product("MTShirtMed", "clothing", 19.99, 5), \
                                      Product("MTShirtLarge", "clothing", 29.99, 5),\
                                      Product("FTShirtSmall", "clothing", 19.99,5),\
                                      Product("FTShirtMed", "clothing", 19.99, 5)],\
                         "electronics": [Product("MacBookPro", "electronics", 2499, 4),\
                                        Product("iPADS", "electronics", 1499, 4),\
                                        Product("iPHONES", "electronics", 1299, 4)],
                         "footwear": [Product("FWFBoots", "footwear", 99.99, 2),\
                                      Product("FWMBoots", "footwear", 69.99, 4) ]}
        self.users = list()
        self.admin = None

    def add_product(self, category, name, price, quantity):
        product = Product(name, category, price, quantity)
        self.products[category].append(product)
        print(f"Successfully added {product}!")

    def update_product(self, category, name, price=None, quantity=None):
        for k, v in self.products.items():
            if k == category:
                for i in v:
                    if i.product_name == name:
                        if price:
                            i.price = price
                        if quantity:
                            i.quantity = quantity
                        print(f"Updated product {i}")

    def remove_product(self, category, name):
        for k, v in self.products.items():
            if k == category:
                for i in v:
                    if i.product_name == name:
                        v.remove(i)
                        print(f"Deleted product {i}")
                        return
        print("Incorrect product category or product name. Check and try again.")

    def view_inventory(self):
        for category, products in self.products.items():
            print(category)
            for product in products: # Product: {i[0].product_name}, Cart Qty: {i[1]}, Amount: {i[2]}
                print(f"Product: {product.product_name}, Unit Price: {product.price}, Qty: {product.quantity}")
                # print(product)


    def admin_interface(self, username):
        print()
        print(f"admin: @{username}")
        print("What would you like to do?")
        print(" - Add product (Enter A)")
        print(" - Update product (Enter U)")
        print(" - Remove product (Enter R)")
        print(" - View inventory (Enter I)")
        print(" - Exit application (Enter E)")

        user_input = input()
        if user_input == "A":
            product_category = input("Product Category: ")
            product_name = input("Product Name: ")
            product_price = input("Product Price: ")
            product_quantity = input("Product Quantity: ")
            self.add_product(product_category, product_name, product_price, product_quantity)
        elif user_input == "U":
            quantity = None
            price = None
            if input("Would you like to update quantity? (Y / N) ") == "Y":
                quantity = input("New quantity: ")
            if input("Would you like to update price? (Y / N) ") == "Y":
                price = input("New price: ")
            self.update_product(quantity, price)
        elif user_input == "R":
            cat = input("What is the category of the product you want to remove? ")
            nm = input("What is the name of the product you want to remove? ")
            self.remove_product(cat, nm)
        elif user_input == "I":
            self.view_inventory()
        elif user_input == "E":
            exit()
        # elif user_input == "S":
        self.admin_interface(username)

    def user_interface(self, user, username):
        print()
        print(f"admin: @{username}")
        print("What would you like to do?")
        print(" - Shop Around (Enter S) ") # this is view inventory but for a user (which means looking around
        print(" - Add product to cart (Enter A) ")
        print(" - View cart (Enter V) ")
        print(" - Update cart (Enter U) ")
        print(" - Remove cart (Enter R) ")
        print(" - All you can buy")
        print(" - Abandon cart")
        print(" - Exit application (Enter E)")

        user_command = input()
        if user_command == "S":
            self.view_inventory()
        elif user_command == "A":
            cat = input("Category: ")
            nm = input("Product: ")
            qty = input("Purchase Quantity: ")
            for k, v in self.products.items():
                if k == cat:
                    for i in v:
                        if i.product_name == nm and qty <= i.quantity:
                            user.cart.add(i, qty)
                            print(f"You've added {nm} of quantity {qty} to your cart.")
        elif user_command == "V":
            user.cart.view()
        elif user_command == "U":
            pass
        elif user_command == "R":
            pass
        elif user_command == "E":
            exit()


        self.user_interface(user, username)








# inter = Interface()
# inter.add_product("electronics", "ipad air", 1399.99, 2)
# inter.update_product("electronics", "ipad air", 1699.99, 5)
# inter.remove_product("footwear", "FWFBoots")
# inter.view_inventory()
